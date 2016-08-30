#!/usr/bin/env bash

GO=go
NAME={{cookiecutter.project_slug}}
TARGET=release

.PHONY: all clean release

all: release

release:

	GOOS=windows GOARCH=386 ${GO} build  -o ${TARGET}/win32/${NAME}.exe -ldflags -w src/main.go
	GOOS=windows GOARCH=amd64 ${GO} build  -o ${TARGET}/win64/${NAME}.exe -ldflags -w src/main.go
	GOOS=linux GOARCH=386 ${GO} build  -o ${TARGET}/linux32/${NAME} -ldflags -w src/main.go
	GOOS=linux GOARCH=amd64  ${GO} build  -o ${TARGET}/linux64/${NAME} -ldflags -w src/main.go
	