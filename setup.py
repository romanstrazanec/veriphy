# -*- coding: UTF-8 -*-
from distutils.core import setup
from hashlib import algorithms_guaranteed

setup(
    name='veriphy',
    version='1.0',
    packages=['veriphy'],
    description='Python script to verify file integrity',
    author='Roman Stražanec',
    author_email='roman.strazanec@student.ukf.sk',
    url='https://github.com/romanstrazanec/veriphy',
    keywords=['verify', 'file', 'signature', 'script', *algorithms_guaranteed],
)
