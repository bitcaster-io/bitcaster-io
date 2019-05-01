DEVELOP?=0
DOCKER_PASS?=
DOCKER_USER?=
TARGET?=0.3.0a0
BUILD_DATE:="$(shell date +"%Y-%m-%d %H:%M")"
# below vars are used internally
BUILD_OPTIONS?=--squash
CMD?=
CONTAINER_NAME?=bitcaster-io
DOCKER_IMAGE_NAME=bitcaster/bitcaster-io
DOCKER_IMAGE=${DOCKER_IMAGE_NAME}:${TARGET}
DOCKERFILE?=Dockerfile
RUN_OPTIONS?=
PIPENV_ARGS?=

help:
	@echo "dev                  build dev image (based on local code)"
	@echo "build                build production image (based on tag ${TARGET})"
	@echo "release              release tag ${TARGET} on docker hub"
	@echo "run                  run ${DOCKER_IMAGE} locally"
	@echo "ignore               run ${DOCKER_IMAGE} locally"
	@echo "bump	 				bump version"


build:
	cd .. && docker build \
			${BUILD_OPTIONS} \
			--build-arg DEVELOP=${DEVELOP} \
			--build-arg VERSION=${TARGET} \
			--build-arg BUILD_DATE=${BUILD_DATE} \
			-t ${DOCKER_IMAGE} \
			-f docker/${DOCKERFILE} .
	docker images | grep ${DOCKER_IMAGE_NAME}


.run:
	mkdir -p ../${VOLUME}
	cd .. && docker run \
	 		--rm \
	 		--name=${CONTAINER_NAME} \
			-p 5000:5000 \
			${RUN_OPTIONS} \
			${DOCKER_IMAGE} \
			${CMD}

local:
	RUN_OPTIONS="-v ${PWD}/..:/code -e PYTHONPATH=/code -it" \
	CMD="/bin/bash" \
	$(MAKE) .run

release:
	pass docker/saxix | docker login -u saxix --password-stdin
	docker tag ${DOCKER_IMAGE_NAME}:${TARGET} ${DOCKER_IMAGE_NAME}:latest
	docker push ${DOCKER_IMAGE_NAME}:latest
	docker push ${DOCKER_IMAGE_NAME}:${TARGET}

deploy:
	lazo rancher --insecure upgrade bitcaster:bitcaster-io bitcaster/bitcaster-io:${TARGET}
#	$(MAKE) bump

bump:
	cd .. && bumpversion --config-file=.bumpversion.cfg num --commit

run:
	$(MAKE) .run
