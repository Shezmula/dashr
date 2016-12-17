# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='dashr',
    version='0.1',
    description='The funniest joke in the world',
    url='http://github.com/carloe/dashr',
    author='Carlo Eugster',
    author_email='carlo@relaun.ch',
    license='MIT',
    packages=['dashr'],
    zip_safe=False,
    install_requires=[
        'requests',
    ],
)
