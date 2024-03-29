#!/usr/bin/env python3

from pathlib import PurePath as Path

from setuptools import Extension, setup
from setuptools.command.build import build
from setuptools.command.build_ext import build_ext
from wheel.bdist_wheel import bdist_wheel

from tree_sitter import Language

class Build(build):
    def run(self):
        source = Path(__file__).with_name('queries')
        dest = Path(self.build_lib) / 'tree_sitter_pymanifest' / 'queries'
        self.copy_tree(str(source), str(dest))
        super().run()

class BuildExt(build_ext):
    def copy_extensions_to_source(self):
        lib_file = Path(__file__).parent.joinpath(
            'bindings', 'python',
            'tree_sitter_pymanifest',
            self._ts_lib.name
        )
        self.copy_file(str(self._ts_lib), str(lib_file))

    def build_extension(self, _):
        self._ts_lib = Path(self.build_lib).joinpath(
            'tree_sitter_pymanifest',
            'pymanifest' + self.compiler.shared_lib_extension
        )
        Language.build_library(str(self._ts_lib), [''])


class BdistWheel(bdist_wheel):
    def get_tag(self):
        python, abi, platform = super().get_tag()
        if python.startswith('cp'):
            python, abi = 'cp39', 'abi3'
        return python, abi, platform


setup(
    packages=['tree_sitter_pymanifest'],
    package_dir={'': 'bindings/python'},
    package_data={
        'tree_sitter_pymanifest.queries': ['*.scm']
    },
    ext_modules=[
        Extension(
            name='tree_sitter_pymanifest',
            sources=['pymanifest'],
            py_limited_api=True
        )
    ],
    cmdclass={
        'bdist_wheel': BdistWheel,
        'build_ext': BuildExt,
        'build': Build
    }
)
