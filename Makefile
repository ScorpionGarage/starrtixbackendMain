run:
	@python3 manage.py runserver

migrate:
	@python3 manage.py makemigrations
	@python3 manage.py migrate

build-dev:
	@docker build -f Dockerfile.dev -t rolandeke/starrtix-api:dev-1.0.0 .
run-dev:
	@docker run --name starrtix -p8000:8000 rolandeke/starrtix-api:dev-1.0.0

build-prod:
	@docker build -f Dockerfile.prod -t rolandeke/starrtix-api:production .
push-prod-images:
	@docker push rolandeke/starrtix-api:production
run-prod:
	@ENV=production docker compose --env-file=./starrtixbackend/.env -f docker-compose-prod.yml up -d
stop-prod:
	@ENV=production docker compose --env-file=./starrtixbackend/.env -f docker-compose-prod.yml down


