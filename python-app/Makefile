
IMAGE=yoavklein3/python-http-server
VERSION=0.1


.PHONY: build-image
build-image:
	docker build -t ${IMAGE}:${VERSION} .

.PHONY: push
push: build-image
	docker push ${IMAGE}:${VERSION}

.PHONY: run-container
run-container: build-image
	docker run --name python-http-server -p 8000:8000 -d --rm ${IMAGE}:${VERSION}

.PHONY: stop-container
stop-container:
	docker container stop python-http-server
