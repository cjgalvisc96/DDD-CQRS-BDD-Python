import uvicorn
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.apps.inventary.api.dependecy_injection import InventaryContainer
from src.apps.inventary.api.routes import router
from src.contexts.shared.domain import DomainException, Logger
from src.contexts.shared.infrastucture import DBConnection


class InventaryAPI:
    def __init__(self, *, port: int, logger: Logger, db: DBConnection) -> None:
        self.port = port
        self.logger = logger
        self.db = db
        self.app = FastAPI()
        self._create_app()

    def _add_dependency_injection(self) -> None:
        self.app.container = InventaryContainer()

    def _add_router(self) -> None:
        self.app.include_router(router=router, prefix="/api")

    def _add_middleware(self) -> None:
        self.app.add_middleware(
            middleware_class=CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def _add_database(self):
        @self.app.on_event("startup")
        async def startup() -> None:
            await self.db.init_db()
            self.logger.info(message="DB is Up!")

    def _add_domain_exceptions(self) -> None:
        @self.app.exception_handler(DomainException)
        async def domain_exception(request, exc):
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "error": str(exc),
                },
            )

    def _create_app(self):
        self._add_dependency_injection()
        self._add_router()
        self._add_database()
        self._add_middleware()
        self._add_domain_exceptions()

    def start(self):
        self.logger.info(
            message=f"Inventary App is running at http://localhost:{self.port}"
        )
        self.logger.info(message="Press CTRL-C to stop")
        uvicorn.run(app=self.app, port=self.port, log_level="info")
