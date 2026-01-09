"""
devroid setup.py
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="devroid",
    version="0.1.0",
    author="Florian",
    description="A utility library for Pycord bots with colored console outputs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nowaroid-Studios/devroid",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "py-cord>=2.0.0",
    ],
    keywords="discord pycord bot utility colors console",
    project_urls={
        "Bug Tracker": "https://github.com/Nowaroid-Studios/devroid/issues",
        "Source": "https://github.com/Nowaroid-Studios/devroid",
    },
)
