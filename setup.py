#
# setup.py
#

from setuptools import setup, find_packages


setup(
  name= "growler",
  version= "0.1.0",
  author= "Andrew Kubera",
  license= "Apache v2.0",
  url= "https://github.com/pyGrowler/growler-indexer",
  author_email= "andrew.kubera@gmail.com",
  description = "Middleware for growler which generates an 'index view' of a directory.",
long_description = """Indexer is middleware for the Growler webframework which
 creates a pretty index view of files and folders within a directory in the
file system. Options can be passed to the middleware to change styles and
viewing rules.""",
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
  install_requires = ['growler']
  packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
)
