#!/usr/bin/env python
from setuptools import setup

try:
    with open('README.md') as fh:
        long_description = fh.read()
except (IOError, OSError):
    long_description = ''

setup(
    name='spect',
    url='https://github.com/con-f-use/spect',
    author='con-f-use',
    author_email='con-f-use@gmx.net',
    description="Shameless name-grab for a possible future project",
    long_description=long_description,
    long_description_content_type='text/markdown',
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    include_package_data=True,
    entry_points={"spect": ["spect = spect"]},
    zip_safe=True,
    options={"bdist_wheel": {"universal": True}},
    package_dir={"": "src"},
    packages=["spect"],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Desktop Environment',
        'Topic :: System :: Shells',
        'Topic :: System :: System Shells',
    ]
)

