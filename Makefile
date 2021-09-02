.PHONY: help

help: ## show this help message and exit
	@echo "usage: make [target]"
	@echo
	@echo "targets:"
	@egrep '^(.+)\:\ ##\ (.+)' ${MAKEFILE_LIST} | column -t -c 2 -s ':#'

build: ## build .alfredworkflow file
	@cd src && zip -q -r ../ip-info.alfredworkflow *

archive: ## archive .zip file
	@make build
	@read -p 'version: ' version; \
	zip -q -r -o /Users/ty0x2333/PycharmProjects/workflow-ip-info/ip-info-$$version.zip ip-info.alfredworkflow