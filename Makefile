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

bdist: release clean
	$(info -> Makefile: building the bdist distribution package ...)
	@(cd src; python3 setup.py bdist)

wheel: release clean
	$(info -> Makefile: building the wheel distribution package ...)
	@(cd src; python3 setup.py bdist_wheel)

push-test:
ifndef TWINE_USERNAME
	$(error Makefile: TWINE_USERNAME is not set - please set it or you won't be able to  authenticate to the PyPI server)
endif
ifndef TWINE_PASSWORD
	$(error Makefile: TWINE_PASSWORD is not set - please set it or you won't be able to  authenticate to the PyPI server)
endif
	$(info -> Makefile: pushing to Test PyPI...)
	@(cd src; twine upload --repository-url https://test.pypi.org/legacy/ dist/*)

push:
ifndef TWINE_USERNAME
	$(error Makefile: TWINE_USERNAME is not set - please set it or you won't be able to  authenticate to the PyPI server)
endif
ifndef TWINE_PASSWORD
	$(error Makefile: TWINE_PASSWORD is not set - please set it or you won't be able to  authenticate to the PyPI server)
endif
	$(info -> Makefile: pushing to PyPI ...)
	@(cd src; twine upload dist/*)

rpm: sdist
	$(info -> Makefile: packaging as RPM ...)
	[ -d ~/rpmbuild ] || mkdir ~/rpmbuild
	[ -d ~/rpmbuild/SOURCES ] || mkdir ~/rpmbuild/SOURCES
	[ -d ~/rpmbuild/SPECS ] || mkdir ~/rpmbuild/SPECS
	mv src/dist/carcano_foolist-${RELEASE}.tar.gz ~/rpmbuild/SOURCES
	cp RPM/SPECS/carcano_foolist.spec ~/rpmbuild/SPECS
	cd ~/rpmbuild/SPECS; rpmbuild --define "_version ${RELEASE}" -ba carcano_foolist.spec
