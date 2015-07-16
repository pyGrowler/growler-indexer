#
# setup.py
#
"""
Middleware for growler which generates an 'index view' of a directory.
"""

import growler.indexer as growler_indexer
from setuptools import setup, find_packages

REQUIRES = [
    'growler'
]

setup(
    name="growler_indexer",
    packages=['growler.indexer'],
    version=growler_indexer.__version__,
    author=growler_indexer.__author__,
    license=growler_indexer.__license__,
    url=growler_indexer.__url__,
    author_email=growler_indexer.__contact__,
    description=__doc__,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        # "Framework :: Growler",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Internet :: WWW/HTTP",
        "Natural Language :: English"
    ],
    platforms=['any'],
    install_requires=REQUIRES
)
