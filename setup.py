# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
    license = f.read()

setup(
    name='robotdialog',
    version='0.1.0',
    description='A sımple unidirectional dialog manager for robots',
    long_description=readme,
    author='Cagatay Odabası',
    author_email='cagatayodabasi91@gmail.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests'))
)
