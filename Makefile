.PHONY: install install-dev test lint format compile-deps clean

PYTHON := python
PIP := pip

install:
	$(PIP) install -r requirements.txt

install-dev:
	$(PIP) install -r requirements-dev.txt

test:
	pytest tests/ -v --cov=. --cov-report=term-missing --cov-report=html

lint:
	flake8 . --exclude=venv,__pycache__,.git,htmlcov --max-line-length=100

format:
	black . --exclude="/(venv|__pycache__|.git|htmlcov)/"

compile-deps:
	pip-compile requirements.in --output-file requirements.txt
	pip-compile requirements-dev.in --output-file requirements-dev.txt

upgrade-deps:
	pip-compile --upgrade requirements.in --output-file requirements.txt
	pip-compile --upgrade requirements-dev.in --output-file requirements-dev.txt

clean:
	rm -rf __pycache__ .pytest_cache htmlcov .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
