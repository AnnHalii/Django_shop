IMAGE ?= my_site_web:develop
COMPOSE ?= docker-compose

.EXPORT_ALL_VARIABLES:

.default: run

run:  docker-build
	$(COMPOSE) up -d

stop:
	$(COMPOSE) stop

logs:
	$(COMPOSE) logs -f web

exec:
	docker exec -it my_site_web_1 bash

docker-build:
	docker build -t $(IMAGE) .
