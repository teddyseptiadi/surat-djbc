# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in pte/__init__.py
from pte import __version__ as version

setup(
	name='pte',
	version=version,
	description='Aplikasi manajemen Perusahaan',
	author='UMIS',
	author_email='teddy@umis.co.id',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
