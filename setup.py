#!/usr/bin/env python3
# coding = utf8
"""
@ Author : ZeroSeeker
@ e-mail : zeroseeker@foxmail.com
@ GitHub : https://github.com/ZeroSeeker
@ Gitee : https://gitee.com/ZeroSeeker
"""
import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="envx",
    version="0.0.1",
    author="ZeroSeeker",
    author_email="zeroseeker@foxmail.com",
    description="make it easy to use env",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/ZeroSeeker/envx",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # install_requires=['colorama==0.4.4']
)