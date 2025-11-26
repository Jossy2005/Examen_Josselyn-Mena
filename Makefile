.PHONY: build run test

build:
	docker build -t ghcr.io/$(USER)/bastidas:1.0.5 .

run:
	python app.py

test:
	pytest -q



