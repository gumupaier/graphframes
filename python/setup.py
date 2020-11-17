# Your python setup file. An example can be found at:
# https://github.com/pypa/sampleproject/blob/master/setup.py
# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 3:04 下午
# @File    : setup.py
from setuptools import setup

setup(name='graphframes',
      version='0.7.0',
      packages=['graphframes', 'graphframes.lib', 'graphframes.examples'],
      install_requires=[
          'nose==1.3.3',
          'numpy>=1.7'
      ],
      )