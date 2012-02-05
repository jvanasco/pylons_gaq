"""pylons_gaq installation script.
"""
import os

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.txt")).read()
README = README.split("\n\n", 1)[0] + "\n"

requires = [
    "pylons", 
    ]

setup(name="pylons_gaq",
      version="0.0.4",
      description="Lightweight Google Analytics support for pylons",
      long_description=README,
      classifiers=[
        "Intended Audience :: Developers",
        "Framework :: Pylons",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        ],
      keywords="web pylons",
      py_modules=['pylons_gaq'],
      author="Jonathan Vanasco",
      author_email="jonathan@findmeon.com",
      url="https://github.com/jvanasco/pylons_gaq",
      license="MIT",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      tests_require = requires,
      install_requires = requires,
      )

