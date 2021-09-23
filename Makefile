.PHONY: help
WORKFLOW_VERSION := `plutil -extract version xml1 -o - src/info.plist | sed -n "s/.*<string>\(.*\)<\/string>.*/\1/p"`

help: ## show this help message and exit
	@echo "usage: make [target]"
	@echo
	@echo "targets:"
	@egrep '^(.+)\:\ ##\ (.+)' ${MAKEFILE_LIST} | column -t -c 2 -s ':#'

update_version: ## update workflow version
	@read -p 'version: ' version; \
	plutil -replace version -string $$version src/info.plist;

version: ## get current workflow version
	@echo "${WORKFLOW_VERSION}"

build: ## build .alfredworkflow file
	@make clean;
	@mkdir -p dist;
	@cd src && zip -q -r ../dist/ip-info.alfredworkflow *

clean: ## Clean build and archive files
	@rm -rf dist;

archive: ## archive .zip file
	@make build; \
	version=${WORKFLOW_VERSION}; \
	cd dist && zip -q -r -o ip-info-$$version.zip ip-info.alfredworkflow