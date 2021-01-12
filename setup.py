#! /usr/bin/env python
"""Density Peak Advanced clustering algorithm, scikit-learn compatible."""
import codecs
import os
import numpy

from setuptools import find_packages
from numpy.distutils.core import Extension, setup
from Cython.Build import cythonize

numpy_include_dir = numpy.get_include()

# get __version__ from _version.py
ver_file = os.path.join('Pipeline', '_version.py')
with open(ver_file) as f:
    exec(f.read())

DISTNAME = 'DPApipeline'
DESCRIPTION = 'The Density Peak Advanced packages.'

with codecs.open('README.rst', encoding='utf-8-sig') as f:
    LONG_DESCRIPTION = f.read()

with open('requirements.txt') as f:
    INSTALL_REQUIRES = f.read().splitlines()

LICENSE = 'new BSD'
VERSION = __version__
CLASSIFIERS = ['Intended Audience :: Science/Research',
               'Intended Audience :: Developers',
               'License :: OSI Approved',
               'Programming Language :: Python',
               'Topic :: Software Development',
               'Topic :: Scientific/Engineering',
               'Operating System :: Microsoft :: Windows',
               'Operating System :: POSIX',
               'Operating System :: Unix',
               'Operating System :: MacOS',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3.5',
               'Programming Language :: Python :: 3.6',
               'Programming Language :: Python :: 3.7']

EXTRAS_REQUIRE = {
    'tests': [
        'pytest',
        'pytest-cov'],
    'docs': [
        'sphinx',
        'sphinx-gallery',
        'sphinx_rtd_theme',
        'numpydoc',
        'matplotlib'
    ]
}

def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    import numpy
    config = Configuration('DPApipeline', parent_package, top_path)
    config.add_subpackage('DPA')
    return config

EXTENSIONS = [
    Extension(
        name='Pipeline._DPA',
        sources=['Pipeline/_DPA.pyx'],
        include_dirs=[numpy_include_dir],
        define_macros=[('CYTHON_TRACE', '1')],
        extra_compile_args=['-O3'],
        ),
    Extension(
        name='Pipeline._PAk',
        sources=['Pipeline/_PAk.pyx'],
        include_dirs=[numpy_include_dir],
        define_macros=[('CYTHON_TRACE', '1')],
        extra_compile_args=['-O3'],
        ),
    Extension(
        name='Pipeline.NR',
        sources=['Pipeline/NRmaxL.f90']
    )
    ]


setup(name=DISTNAME,
      description=DESCRIPTION,
      author="Maria d'Errico",
      license=LICENSE,
      version=VERSION,
      long_description=LONG_DESCRIPTION,
      zip_safe=False,  # the package can run out of an .egg file
      classifiers=CLASSIFIERS,
      packages=find_packages(exclude=['notebooks']),
      install_requires=INSTALL_REQUIRES,
      extras_require=EXTRAS_REQUIRE,
      ext_modules=cythonize(EXTENSIONS))
      #**configuration(top_path='').todict())
