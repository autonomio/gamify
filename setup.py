#! /usr/bin/env python
#
# Copyright (C) 2019 Mikko Kotila

DESCRIPTION = "Talos Hyperparameter Tuning for Keras"
LONG_DESCRIPTION = """\
Gamify puts the researcher back in the driver's seat in modern deep
learning workflow by unlocking a new era of man-machine symbiosis
in artificial intelligence model development. As the mission matures,
developing state-of-the-art deep learning models will feel more like
playing a Real-Time Strategy Game.
"""

DISTNAME = 'gamify'
MAINTAINER = 'Mikko Kotila'
MAINTAINER_EMAIL = 'mailme@mikkokotila.com'
URL = 'http://autonom.io'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/autonomio/gamify/'
VERSION = '0.0.1'

try:
    from setuptools import setup
    _has_setuptools = True
except ImportError:
    from distutils.core import setup

install_requires = ['flask']


if __name__ == "__main__":

    setup(name=DISTNAME,
          author=MAINTAINER,
          author_email=MAINTAINER_EMAIL,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          install_requires=install_requires,
          packages=['gamify'],

          classifiers=['Intended Audience :: Science/Research',
                       'Programming Language :: Python :: 2.7',
                       'Programming Language :: Python :: 3.5',
                       'Programming Language :: Python :: 3.6',
                       'License :: OSI Approved :: MIT License',
                       'Topic :: Scientific/Engineering :: Human Machine Interfaces',
                       'Topic :: Scientific/Engineering :: Artificial Intelligence',
                       'Topic :: Scientific/Engineering :: Mathematics',
                       'Operating System :: POSIX',
                       'Operating System :: Unix',
                       'Operating System :: MacOS',
                       'Operating System :: Microsoft :: Windows :: Windows 10'])
