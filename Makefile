VENV = venv/bin

.PHONY: help clean lint fmt test pre-commit run

help:
	@echo ""
	@echo "Use 'make <command>'"
	@echo ""
	@echo "commands"
	@echo "  venv        create venv and install project"
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
	@$(VENV)/pip install -U pip
	@$(VENV)/pip install -r requirements.txt -r requirements-dev.txt
	@$(VENV)/pip install -e .

clean:
	-@rm -rf venv
	-@rm -fr `find . -name __pycache__`

lint:
	@$(VENV)/flake8 \
		pipeline \
		data \
		run.py

fmt:
	@$(VENV)/isort .
	@$(VENV)/black .

test: lint
	@$(VENV)/pytest

pre-commit: test fmt

run: venv
	@$(VENV)/python run.py