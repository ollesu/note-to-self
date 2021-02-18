# How to check for variables and binaries in Makefiles

AWS_CLI_VERSION := $(shell aws --version 2>/dev/null)
ifndef AWS_CLI_VERSION
$(error aws cli is not installed. it is required to use this Makefile)
endif

ifndef ENV
$(error ENV is not set. run 'export ENV=dev|prod' to further use this Makefile)
endif

ifeq ($(ENV), dev)
else ifeq ($(ENV), prod)
else
$(error ENV=${ENV} is not dev nor prod)
endif

