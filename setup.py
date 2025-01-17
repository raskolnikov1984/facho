#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is part of facho.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0',
                'chardet>=0.0',
                'zeep==4.0.0',
                'lxml==4.6.3',
                'cryptography==3.3.2',
                'pyOpenSSL==20.0.1',
                'xmlsig==0.1.7',
                'xades==0.2.2',
                'xmlsec==1.3.12',
                # usamos esta dependencia en runtime
                # para forzar uso de policy_id de archivo local
                'mock>=2.0.0',
                'xmlschema>=1.8']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Jovany Leandro G.C",
    author_email='bit4bit@riseup.net',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Facturacion Electronica Colombia",
    entry_points={
        'console_scripts': [
            'facho=facho.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.gc', '*.xsd', 'politicadefirmav2.pdf']
    },
    keywords='facho',
    name='facho',
    packages=find_packages(exclude=("tests",)),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/bit4bit/facho',
    version='0.2.0',
    zip_safe=False,
)
