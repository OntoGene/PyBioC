#!/usr/bin/env python
# coding: utf8

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(name='PyBioC',
      version='1.02-lf.1',
      author='Hernani Marques',
      author_email='h2m@access.uzh.ch',
      description='Python library to deal with BioCreative XML data',
      long_description=readme,
      packages=find_packages())
