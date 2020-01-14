#!/usr/bin/env python
import re, time, datetime
from setuptools import setup

try:
    with open('README.md') as fh:
        README = fh.read()
    description = next(s for s in README.splitlines()[2:] if re.match(r"^\w", s))
except (IOError, OSError):
    README = description = ''


def loc_vers(*a, **kw):
    import dateutil.parser

    scm = a[0]
    mems = '{distance=}, {dirty=}, {branch=}, {node=}, {tag=}, {time'
    for mem in mems.split('=}, '):
        mem = mem.strip('{')
        print(f'{mem} {type(scm.__dict__[mem])}= {scm.__dict__[mem]}')
    print(scm.time.tzname())
    print("\n")
    return ""


setup(
    name='spect',
    url='https://github.com/con-f-use/spect',
    author='con-f-use',
    author_email='con-f-use@gmx.net',
    description=description,
    long_description=README,
    long_description_content_type='text/markdown',
    use_scm_version=dict(local_scheme=loc_vers),
    setup_requires=["setuptools_scm", "python-dateutil"],
    include_package_data=True,
    zip_safe=True,
    options={"bdist_wheel": {"universal": True}},
    package_dir={"": "src"},
    packages=["spect"],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Desktop Environment',
    ],
)
