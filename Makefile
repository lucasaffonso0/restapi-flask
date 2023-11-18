APP = restapi

test:
	@flake8 . --exclude .venv
	@pytest -v --disable-warnings
	
compose:
	@docker-compose build
	@docker-compose up

run:
	@docker-compose up

heroku:
	@heroku container:login
	@sudo heroku container:push -a jlrestapiflask web
	@sudo heroku container:release -a jlrestapiflask web