import os

from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def requirements(fname):
    for line in open(os.path.join(os.path.dirname(__file__), fname)):
        yield line.strip()

version = "0.1.6"

setup(
    name="wb_vandalism",
    version=version,
    author="Amir Sarabadani",
    author_email="Ladsgroup@gmail.com",
    description=("A library for performing automatic detection of vandalism in Wikidata."),
    license="MIT",
    url="https://github.com/Ladsgroup/wb-vandalism",
    packages=find_packages(),
    long_description=read('README.rst'),
    install_requires=list(requirements('requirements.txt')),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Topic :: Scientific/Engineering"
    ],
)
