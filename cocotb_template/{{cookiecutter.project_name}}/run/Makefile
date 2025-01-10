
.PHONY: tests help clean clean_all

PWD=$(shell pwd)

PYTEST_ARGS ?= -o log_cli=True --html=report.html --self-contained-html --disable-warnings
NUM_CORES ?= 10 # Number of workers to use with pytest-xdist (parallel execution), change if needed
.DEFAULT_GOAL := help

help:  ## Show this help, executed by default
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.venv: ## Set up the virtual environment
	@echo "Setting up virtual environment..."
	@python3.9 -m venv .venv

requirements: requirements.txt .venv ## Install requirements and set up the virtual environment, run before the first test
	@echo "Installing requirements..."
	@source .venv/bin/activate && pip install --upgrade pip && pip install -r $< && touch $@

tests: ## Run tests with pytest and waveform exit
	@echo "Running pytest with waveform output..."
	@source .venv/bin/activate && PYTHONPATH=$(PWD)/.. pytest $(PYTEST_ARGS) -n $(NUM_CORES)

clean: ## Clean up the generated files (add the removal of simulator files)
	@echo "Cleaning up generated files..."
	@find .. -name "__pycache__" -type d -exec rm -rf {} +
	@rm -rf __pycache__
	@rm -rf .pytest_cache
	@rm -rf pytest*
	@rm -f report.html
	@rm -f .coverage

clean_all: clean ## Clean up the generated files, the virtual environment and the requirements
	@echo "Cleaning up the virtual environment and the requirements..."
	@rm -rf .venv
	@rm -f requirements