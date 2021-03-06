#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import ast
from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), 'rb') as readme_file:
    readme = readme_file.read().decode('utf-8')


_version_re = re.compile(r'__version__\s+=\s+(.*)')


with open('{{ cookiecutter.package_name }}/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


with open(path.join(here, 'requirements.txt'), 'rb') as f:
    all_reqs = f.read().decode('utf-8').split('\n')


install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]


setup(
    name='{{ cookiecutter.package_name }}',
    version=version,
    description="",
    long_description=readme,
    author="{{ cookiecutter.author_name }}",
    author_email='{{ cookiecutter.author_email }}',
    url='https://github.com/{{ cookiecutter.author_name }}/{{ cookiecutter.package_name }}',
    packages=find_packages(),
    package_dir={},
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.package_name }}={{ cookiecutter.package_name }}.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=install_requires,
    dependency_links=dependency_links,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='{{ cookiecutter.package_name }}',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
