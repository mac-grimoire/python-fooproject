all: unittests

clean:
	$(info -> Makefile: cleanup previous builds ... )
	@(rm -rf src/test/__pycache__ src/carcano/foolist/__pycache__ src/bin/__pycache__)
	@(rm -rf src/carcano_foolist.egg-info src/.eggs)
	@(rm -rf src/dist src/build)

release:
ifndef RELEASE 
	$(error Makefile: RELEASE is not set - please set it with a value with the following format: major.minor[.patch][sub] - for example 0.0.1 or 1.0.1-a2)
endif
	$(info -> Makefile: validating RELEASE=${RELEASE} format)
	@(echo ${RELEASE} |grep -qE "[0-9]+\.[0-9]+\.*[0-9]*[a-zA-Z]*[0-9]*") || (echo " ${RELEASE} is not in compliance with our version format"; exit 1)	
	@(cd src; sed -i -E "s/version='[0-9]+.[0-9]+\.*[0-9]+[a-zA-Z]*[0-9]*'/version='${RELEASE}'/g" setup.py)

unittests:
	$(info -> Makefile: Launching unit tests ...)
	@(cd src; python3 setup.py nosetests >/dev/null)

sdist: release clean
	$(info -> Makefile: building the sdist distribution package ...)
	@(cd src; python3 setup.py sdist)
