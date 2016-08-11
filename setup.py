from __future__ import print_function

import io
import os
import os.path
import re
from distutils.text_file import TextFile

from setuptools import find_packages, setup

home = os.path.abspath(os.path.dirname(__file__))
missing = object()


def read_description(*files, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = [io.open(name, encoding=encoding).read() for name in files]
    return sep.join(buf)


def read_dependencies(requirements=missing):
    if requirements is None:
        return []
    if requirements is missing:
        requirements = 'requirements.txt'
    if not os.path.isfile(requirements):
        return []
    text = TextFile(requirements, lstrip_ws=True)
    try:
        return text.readlines()
    finally:
        text.close()


def read_version(version_file):
    with open(version_file, 'rb') as fd:
        result = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                           fd.read(), re.MULTILINE)
        return result.group(1) if result else '0.0.1'


def collect_resource(resource, prefix='.'):
    resources = []
    for current_dir, _, files in os.walk(resource):
        if files:
            resources.append((os.path.join(prefix, current_dir), [os.path.join(current_dir, f) for f in files]))
    return resources


setup(
    name='recipe',
    version=read_version('recipe/__init__.py'),
    url="http://trgit2/dfis/recipe",
    license='The MIT License',
    description='just a simplesirius',
    author='DFIS',
    install_requires=read_dependencies(),
    include_package_data=True,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'recipe = recipe.main:main'
        ]

    },

    data_files=collect_resource('templates', prefix='recipe'),
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Software Distribution',
        'Topic :: System :: Systems Administration',
    ]
)
