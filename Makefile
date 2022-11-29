build_no_cache:
	docker-compose build --no-cache

build:
	docker-compose build

start:
	docker-compose up

stop:
	docker-compose down

# ✅ Tests and Coverage
coverage:
	docker-compose run api coverage run  -m pytest tests/ --disable-warnings -s && coverage report -m

all_test:
	docker-compose run api pytest tests --disable-warnings

unit_test:
	docker-compose run api pytest -v -m unit --disable-warnings

feature_test:
	docker-compose run api pytest -v -m feature --disable-warnings
