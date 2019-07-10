PYTHON ?= python3
PIP ?= pip3

ROOT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

.PHONY:

all: list

list:
	@echo "The following targets are available:"
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

install: .PHONY
	@echo "-------------------------------------------------------"
	@echo "Using ${PIP} to install dependencies in user space"
	@echo "--------------------------------------------------"
	${PIP} install --user -r requirements.txt

clean: .PHONY
	@echo "-------------------------------------------------------"
	@echo "Using custom script to locate and delete cache files"
	@echo "-------------------------------------------------------"
	${PYTHON} tools/cleanup.py
	@echo "----------------------------------------------------"
	@echo "Removing html documentation built"
	@echo "----------------------------------------------------"
	@if [ -d "doc/build" ]; then \
		rm -r doc/build; \
		echo "Done."; \
	else \
		echo "Nothing to do."; \
	fi
	@echo "----------------------------------------------------"
	@echo "Removing temporary project files"
	@echo "----------------------------------------------------"
	@if [ -f ".coverage" ]; then \
		rm .coverage; \
	fi
	@if [ -d "coverage/html" ]; then \
		rm -r coverage/html; \
	fi
	@echo "Done."

check: .PHONY
	@echo "-------------------------------------------------------"
	@echo "Checking syntax and spelling in modified files"
	@echo "-------------------------------------------------------"
	PYTHONPATH=$(ROOT_DIR) ${PYTHON} -m pylint app/main.py

test: clean
	@echo "-------------------------------------------------------"
	@echo "Running all unit tests gathered from the test/ folder"
	@echo "-------------------------------------------------------"
	PYTHONPATH=$(ROOT_DIR) ${PYTHON} -m coverage run test/collection_full.py
	@echo "-------------------------------------------------------"
	@echo "Compiling code coverage statistics"
	@echo "-------------------------------------------------------"
	PYTHONPATH=$(ROOT_DIR) ${PYTHON} -m coverage report -m

coverage: test
	@echo "-------------------------------------------------------"
	@echo "Building HTML code coverage report"
	@echo "-------------------------------------------------------"
	PYTHONPATH=$(ROOT_DIR) ${PYTHON} -m coverage html
