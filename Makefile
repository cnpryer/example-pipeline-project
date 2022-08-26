.PHONY: help clean lint fmt mt-check test pre-commit run dashboard-start dashboard-agent

help:
	@echo ""
	@echo "Use 'make <command>'"
	@echo ""
	@echo "commands"
	@echo "  .venv              create venv and install dependencies"
	@echo "  clean              remove cleanable files"
	@echo "  lint               run linters"
	@echo "  fmt                run formaters"
	@echo "  fmt-check          run formatting check"
	@echo "  test               run all tests"
	@echo "  pre-commit         run pre-commit standardization"
	@echo "  dashboard-start    start prefect dashboard (docker required)"
	@echo "  dashboard-agent    create prefect local dashboard agent"
	@echo ""
	@echo "Check the Makefile to know exactly what each target is doing."

.venv:
	@python -m venv .venv
	@poetry install
	@pre-commit install

clean:
	-@rm -rf .venv
	-@rm -fr `find . -name __pycache__`
	-@rm -rf .pytest_cache
	-@rm -rf .mypy_cache

lint: .venv
	@poetry run flake8 \
		business \
		core \
		data \
		tests \
		run.py

fmt: .venv
	@poetry run isort .
	@poetry run black .

fmt-check: .venv
	@poetry run isort . --check
	@poetry run black . --check

test: .venv
	@poetry run pytest

pre-commit: test fmt
	@poetry run mypy \
		business \
		core \
		data \
		tests \
		run.py

dashboard-start: .venv
	@poetry run prefect backend server
	@poetry run prefect server start

dashboard-agent: .venv
	@poetry run prefect agent local start
