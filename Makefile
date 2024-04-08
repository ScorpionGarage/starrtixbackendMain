run:
	@python3 manage.py runserver

migrate:
	@python3 manage.py makemigrations
	@python3 manage.py migrate

build-dev:
	@docker build -f Dockerfile.dev -t rolandeke/starrtix-api:dev-1.0.0 .
run-dev:
	@docker run --name starrtix -p8000:8000 rolandeke/starrtix-api:dev-1.0.0