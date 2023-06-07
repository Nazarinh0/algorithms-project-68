install:
	poetry install

lint:
	poetry run flake8 router

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=router tests/ --cov-report xml
