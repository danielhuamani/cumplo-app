docker-local-build:
	docker-compose -f compose/local/docker-compose.yml build
docker-local-run:
	docker-compose -f compose/local/docker-compose.yml up 
docker-local-migrate:
	docker-compose -f compose/local/docker-compose.yml run app python ./src/manage.py migrate
docker-local-migrations:
	docker-compose -f compose/local/docker-compose.yml run app python ./src/manage.py makemigrations	
