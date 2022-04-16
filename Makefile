ACTIVATE = source venv/bin/activate

.PHONY: help clean lint fmt mt-check test pre-commit run dashboard-start dashboard-agent

help:
	@echo ""
	@echo "Use 'make <command>'"
	@echo ""
	@echo "commands"
	@echo "  venv               create venv and install dependencies"
	@echo "  clean              remove cleanable files"
	@echo "  lint               run linters"
	@echo "  fmt                run formaters"
	@echo "  fmt-check          run formatting check"
	@echo "  test               run all tests"
	@echo "  pre-commit         run pre-commit standardization"
	@echo "  run                run prepared jobs from run.py"
	@echo "  dashboard-start    start prefect dashboard (docker required)"
	@echo "  dashboard-agent    create prefect local dashboard agent"
	@echo ""
	@echo "Check the Makefile to know exactly what each target is doing."

venv:
	@python -m venv venv
	@$(ACTIVATE) && poetry install

clean:
	-@rm -rf venv
	-@rm -fr `find . -name __pycache__`
	-@rm -rf .pytest_cache

lint: venv
	@$(ACTIVATE) && poetry run flake8 \
		business \
		core \
		data \
		tests \
		run.py

fmt: venv
	@$(ACTIVATE) && poetry run isort . \
		&& poetry run black .

fmt-check: venv
	@$(ACTIVATE) && poetry run isort . --check \
		&& poetry run black . --check

test: venv lint fmt-check
	@$(ACTIVATE) && poetry run pytest

pre-commit: test fmt

run: venv
	@$(ACTIVATE) && poetry run python run.py

dashboard-start: venv
	@$(ACTIVATE) && poetry run prefect backend server \
		&& poetry run prefect server start

dashboard-agent: venv
	@$(ACTIVATE) && poetry run prefect agent local start
