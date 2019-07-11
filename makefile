PYTHON ?= python3
PIP ?= pip3

PRINT_TITLE_HLINE := ${PYTHON} -m tools.pretty_console print-title-hline
PRINT_SUBTITLE_HLINE := ${PYTHON} -m tools.pretty_console print-subtitle-hline

ROOT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

.PHONY:

all: list

list:
	@echo "The following targets are available:"
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

install: .PHONY
	@${PRINT_TITLE_HLINE} "Installing dependencies"
	${PIP} install --user -r requirements.txt

clean: .PHONY
	@${PRINT_TITLE_HLINE} "Cleaning project"

	@${PRINT_SUBTITLE_HLINE} "Removing cached files"
	${PYTHON} tools/cleanup.py

	@${PRINT_SUBTITLE_HLINE} "Removing autogenerated documentation"
	@if [ -d "doc/build" ]; then \
		rm -r doc/build; \
		echo "Done."; \
	else \
		echo "Nothing to do."; \
	fi

	@${PRINT_SUBTITLE_HLINE} "Removing temporary project files"
	@if [ -f ".coverage" ]; then \
		rm .coverage; \
	fi
	@if [ -d "coverage/html" ]; then \
		rm -r coverage/html; \
	fi
	@echo "Done."

check: .PHONY
	@${PRINT_TITLE_HLINE} "Running Checks"

	@${PRINT_SUBTITLE_HLINE} "Checking syntax and grammar"
	PYTHONPATH=$(ROOT_DIR) ${PYTHON} -m pylint app/main.py

test: clean
	@${PRINT_TITLE_HLINE} "Running All Tests"

	@${PRINT_SUBTITLE_HLINE} "Running all unit tests gathered from the test/ folder"
	PYTHONPATH=$(ROOT_DIR) ${PYTHON} -m coverage run -m pytest test/

	@${PRINT_SUBTITLE_HLINE} "Compiling code coverage statistics"
	PYTHONPATH=$(ROOT_DIR) ${PYTHON} -m coverage report -m

coverage: test
	@${PRINT_TITLE_HLINE} "Computing Coverage"

	@${PRINT_SUBTITLE_HLINE}  "Building coverage report"
	PYTHONPATH=$(ROOT_DIR) ${PYTHON} -m coverage html
