docker-local-build:
	docker-compose -f compose/local/docker-compose.yml build
docker-local-run:
	docker-compose -f compose/local/docker-compose.yml up 
docker-local-migrate:
	docker-compose -f compose/local/docker-compose.yml run app python manage.py migrate
docker-local-migrations:
	docker-compose -f compose/local/docker-compose.yml run app python manage.py makemigrations	
create-app:
	@ docker-compose -f compose/local/docker-compose.yml run app  mkdir ./apps/${APP_NAME}
	@ docker-compose -f compose/local/docker-compose.yml run app  python manage.py startapp ${APP_NAME} ./apps/${APP_NAME}
	@ sudo chown -R ${USER}:${USER} ./apps/${APP_NAME}