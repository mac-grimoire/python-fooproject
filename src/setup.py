from setuptools import setup, find_namespace_packages

setup(
    name='carcano_foolist',
    version='0.0.1',
    author='Marco Antonio Carcano',
    author_email='myemailaddress@mydomain.tld',
    url= 'https://github.com/mac-grimoire/python-spells.git',
    packages=find_namespace_packages(include=['carcano.*']),
    setup_requires=['nose>=1.0'],
    test_suite="nose.collector",
    tests_require=["nose"],
)
