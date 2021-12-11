from setuptools import setup, find_namespace_packages

setup(
    name='carcano_foolist',
    version='0.0.1',
    author='Marco Antonio Carcano',
    author_email='myemailaddress@mydomain.tld',
    description='An example list object that exploit Pyhon iteratable facilities',
    classifiers=[
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3'
    ],
    url= 'https://github.com/mac-grimoire/python-spells.git',
    license= 'GNU Lesser General Public License v3 or later',
    keywords = 'iteratable list',
    project_urls={
        'Bug Tracker': 'https://github.com/mac-grimoire/python-spells.git',
        'Documentation': 'https://github.com/mac-grimoire/python-spells.git',
        'Source Code': 'https://github.com/mac-grimoire/python-spells.git',
    },    
    packages=find_namespace_packages(include=['carcano.*']),
    scripts=["bin/fooapp.py"],
    data_files=[
        ("bin", ["bin/logging.conf"]),
        ("share/doc/fooapp/rsyslog", ["share/doc/fooapp/rsyslog/fooapp.conf"])
    ],
    setup_requires=['nose>=1.0'],
    test_suite="nose.collector",
    tests_require=["nose"]
)
