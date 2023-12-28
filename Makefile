APP = jlrestapiflask

test:
	@bandit -r . -x '*/.venv/*','*/tests/*'
	@black .
	@flake8 . --exclude .venv
	@pytest -v --disable-warnings
	
compose:
	@docker-compose build
	@docker-compose up

run:
	@docker-compose up

heroku:
	@heroku container:login
	@heroku container:push -a $(APP) web
	@heroku container:release -a $(APP) web