.PHONY: install install-dev test lint format clean help docker-build docker-run

help:
	@echo "Available commands:"
	@echo "  make install       - Install production dependencies"
	@echo "  make install-dev   - Install development dependencies"
	@echo "  make test          - Run tests with coverage"
	@echo "  make lint          - Run flake8 linter"
	@echo "  make format        - Format code with black"
	@echo "  make clean         - Clean cache and compiled files"
	@echo "  make docker-build  - Build Docker image"
	@echo "  make docker-run    - Run Docker container"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

test:
	pytest tests/ -v --cov=. --cov-report=term-missing --cov-report=html

lint:
	flake8 . --max-line-length=100 --exclude=__pycache__,.git,venv,tests

format:
	black . --line-length=100

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage

docker-build:
	docker build -t pegasus-summarizer .

docker-run:
	docker run --rm pegasus-summarizer
