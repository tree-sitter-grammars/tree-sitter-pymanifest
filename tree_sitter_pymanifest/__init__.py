"""PyPA manifest parser"""

from pathlib import PurePath as _PurePath
from pkgutil import get_data as _get_data
from sys import platform as _platform

from tree_sitter import Language as _Language
from tree_sitter import Parser as _Parser

_language = _Language(
  _PurePath(__file__).with_name('pymanifest') \
    .with_suffix('.dll' if _platform == 'win32' else '.so'),
  'pymanifest'
)

_parser = _Parser()
_parser.set_language(_language)

"""Run a query on the given source code"""
query = _language.query

"""Parse the given source code"""
parse = _parser.parse

def highlights(tree):
  """Return the highlight groups for the given source tree"""
  data = _get_data(__package__, 'queries/highlights.scm')
  return query(data.decode()).captures(tree.root_node)

__author__ = 'ObserverOfTime'
__version__ = '0.1.0'
__license__ = 'MIT'

__all__ = ['parse', 'query', 'highlights']
