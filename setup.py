#!/usr/bin/env python
import os, shutil, glob, re, mimetypes
from setuptools import setup


try:
    from setuptools.command.clean import clean as _clean
except ImportError:
    from distutils.command.clean import clean as _clean


class Clean(_clean):
    def run(self):
        super(Clean, self).run()
        remove = lambda l: not self.dry_run and [shutil.rmtree(d, True) for d in l]
        for pkgdir in self.distribution.package_dir.values():
            remove(glob.glob(os.path.join(pkgdir, "*.egg-info")))
        if self.all:
            remove(['dist', '.eggs'])

def docu(docu_file="README.md"):
    with open(docu_file) as fh:
        readme = fh.read()
    return dict(
        long_description=readme,
        long_description_content_type=mimetypes.guess_type(docu_file)[0],
        description=next(s for s in readme.splitlines()[2:] if re.match(r"^\w", s)), 
    )

setup(
    name="spect",
    url="https://github.com/con-f-use/spect",
    author="con-f-use",
    author_email="con-f-use@gmx.net",
    use_scm_version=dict(local_scheme=lambda _: ""),
    setup_requires=["setuptools_scm"],
    include_package_data=True,
    zip_safe=True,
    options={"bdist_wheel": {"universal": True}},
    cmdclass={"clean": Clean},
    package_dir={"": "src"},
    packages=["spect"],
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    **docu(),
)

