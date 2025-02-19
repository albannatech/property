# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re, ast
from pip._internal.req import parse_requirements

# الحصول على الإصدار من المتغير __version__ في property/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('property/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

requirements = parse_requirements("requirements.txt", session="")

setup(
    name='property',
    version=version,
    description='Property Management',
    author='Opensource Solutions Philippines',
    author_email='info@ossph.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[str(ir.requirement) for ir in requirements],
    dependency_links=[str(ir.link) for ir in requirements if ir.link]
)
