"""pylons_gaq installation script.
"""
import os

from setuptools import setup
from setuptools import find_packages

HERE = os.path.abspath(os.path.dirname(__file__))
long_description = description = "Lightweight Google Analytics support for Pylons"
with open(os.path.join(HERE, "README.md")) as fp:
    long_description = fp.read()

requires = [
    "pylons",
]
tests_require = ["pytest"]
testing_extras = tests_require + []

setup(
    name="pylons_gaq",
    version="0.0.4",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Developers",
        "Framework :: Pylons",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="web pylons",
    py_modules=["pylons_gaq"],
    author="Jonathan Vanasco",
    author_email="jonathan@findmeon.com",
    url="https://github.com/jvanasco/pylons_gaq",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        "testing": testing_extras,
    },
)
