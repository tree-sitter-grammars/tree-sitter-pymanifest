#!/usr/bin/env python3

from pathlib import Path
from sys import platform

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext
from wheel.bdist_wheel import bdist_wheel

from tree_sitter import Language


class BuildExt(build_ext):
  def copy_extensions_to_source(self):
    pass

  def build_extension(self, _):
    lib = Path(__file__).with_name('tree_sitter_pymanifest') / 'pymanifest'
    ext = '.dll' if platform == 'win32' else '.so'
    Language.build_library(str(lib.with_suffix(ext)), [''])


class BdistWheel(bdist_wheel):
  def get_tag(self):
    python, abi, plat = super().get_tag()
    if python.startswith('cp'):
        return 'cp36', 'abi3', plat
    return python, abi, plat


setup(
  name='tree-sitter-pymanifest',
  version='0.1.0',
  license='MIT',
  author='ObserverOfTime',
  author_email='chronobserver@disroot.org',
  keywords=['tree-sitter', 'parser', 'lexer'],
  description='A tree-sitter parser for MANIFEST.in files',
  long_description=Path(__file__).with_name('README.rst').read_text(),
  url='https://github.com/ObserverOfTime/tree-sitter-pymanifest',
  packages=['tree_sitter_pymanifest'],
  package_data={
    'tree_sitter_pymanifest': [
      'pymanifest.so',
      'pymanifest.dll',
      'queries/*.scm'
    ]
  },
  install_requires=['tree-sitter~=0.20'],
  setup_requires=['tree-sitter'],
  ext_modules=[
    Extension(
      name='tree_sitter_pymanifest',
      sources=['pymanifest'],
      py_limited_api=True
    )
  ],
  cmdclass={
    'bdist_wheel': BdistWheel,
    'build_ext': BuildExt
  },
  classifiers=[
    'Development Status :: 2 - Pre-Alpha',
    'License :: OSI Approved :: MIT License',
    'Topic :: Software Development :: Compilers',
    'Topic :: Text Processing :: Linguistic',
  ]
)
