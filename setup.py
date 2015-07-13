# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = '0.1dev'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')

setup(name='collective.monitor',
      version=version,
      description="Monitoring meta package for Zope/Plone installs",
      long_description=long_description,
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Benoît Suttor',
      author_email='bsuttor@imio.be',
      url='https://github.com/collective/collective.monitor',
      license='gpl',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Zope2',
          'five.z2monitor',
          'Products.ZNagios',
          'munin.zope',
          'zc.z3monitor',
          'zc.monitorcache',
          'zc.monitorlogstats',
          'ztfy.monitor'
      ])
