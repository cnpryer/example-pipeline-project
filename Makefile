ACTIVATE = source venv/bin/activate

.PHONY: help clean lint fmt test pre-commit run

help:
	@echo ""
	@echo "Use 'make <command>'"
	@echo ""
	@echo "commands"
	@echo "  venv        create venv and install dependencies"
	@echo "  clean       remove cleanable files"
	@echo "  lint        run linters"
	@echo "  fmt         run formaters"
	@echo "  test        run all tests"
	@echo "  pre-commit  run pre-commit standardization"
	@echo "  run         run prepared jobs from run.py"
	@echo ""
	@echo "Check the Makefile to know exactly what each target is doing."

venv:
	@python -m venv venv
	@$(ACTIVATE) && poetry install

clean:
	-@rm -rf venv
	-@rm -fr `find . -name __pycache__`
	-@rm -rf .pytest_cache

lint:
	@$(ACTIVATE) && poetry run flake8 \
		business \
		core \
		data \
		tests \
		run.py

fmt:
	@$(ACTIVATE) && poetry run isort . \
		&& poetry run black .

test: lint
	@$(ACTIVATE) && poetry run pytest

pre-commit: test fmt

run: venv
	@$(ACTIVATE) && poetry run python run.py