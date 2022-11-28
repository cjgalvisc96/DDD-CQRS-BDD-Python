import time
from uuid import uuid4

import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.apps.inventary.api.dependecy_injection import InventaryContainer
from src.apps.inventary.api.routes import products_router
from src.contexts.shared.domain import DomainException, Logger
from src.contexts.shared.infrastucture import DBConnection


class InventaryAPI:
    def __init__(
        self, *, host: str, port: int, logger: Logger, db: DBConnection
    ) -> None:
        self.host = host
        self.port = port
        self.logger = logger
        self.db = db
        self.app = FastAPI()
        self._create_app()

    def _add_dependency_injection(self) -> None:
        self.app.container = InventaryContainer()

    def _add_routers(self) -> None:
        self.app.include_router(router=products_router, prefix="/api")

    def _add_cors_middleware(self) -> None:
        self.app.add_middleware(
            middleware_class=CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def _add_logger_middleware(self) -> None:
        @self.app.middleware("http")
        async def add_process_time_header(request: Request, call_next):
            start_time = time.time()
            message = (
                f"ID={uuid4()}",
                f"Server={request.scope.get('server')},"
                f"Method={request.scope.get('method')},"
                f"Url={request.scope.get('path')}",
            )
            self.logger.info(message=f"[RequestStart]{message}")
            response = await call_next(request)
            process_time = time.time() - start_time
            self.logger.info(
                message=f"[RequestEnd]{message} => ProccesTime={process_time}"
            )
            return response

    def _add_database(self):
        @self.app.on_event("startup")
        async def startup() -> None:
            await self.db.init_db()
            self.logger.debug(message="DB is Up!")

    def _add_domain_exceptions(self) -> None:
        @self.app.exception_handler(DomainException)
        async def domain_exception(request, exc):
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"error": str(exc), "type": "domain_error"},
            )

    def _create_app(self):
        self._add_dependency_injection()
        self._add_routers()
        self._add_database()
        self._add_cors_middleware()
        self._add_logger_middleware()
        self._add_domain_exceptions()

    def start(self):
        try:
            self.logger.debug(message="Server is Up!")
            uvicorn.run(
                app=self.app, host=self.host, port=self.port, log_level="info"
            )
        except Exception as error:
            self.logger.error(message=f"[ERROR]start()=>{error}")
