build_no_cache:
	docker-compose build --no-cache

build:
	docker-compose build

start:
	docker-compose up

stop:
	docker-compose down

# ✅ Tests and Coverage
test:
	docker-compose run api coverage run  -m pytest tests/ --disable-warnings -s && coverage report -m
