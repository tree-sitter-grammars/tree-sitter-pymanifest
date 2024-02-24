from importlib.resources import files
from pathlib import PurePath
from sys import platform

from tree_sitter import Language, Parser

_language = Language(
    PurePath(__file__).with_name('pymanifest').with_suffix(
        {'win32': '.dll', 'darwin': '.dylib'}.get(platform, '.so')
    ),
    'pymanifest'
)

_parser = Parser()
_parser.set_language(_language)

_highlights = files(__package__) / 'queries' / 'highlights.scm'

def parse(source):
    """Parse the given source code"""
    if isinstance(source, str):
        source = source.encode()
    return _parser.parse(source, keep_text=True)

def query(query, node):
    """Run an arbitrary query on the given source node"""
    return _language.query(query).captures(node)

def highlights(tree):
    """Return the highlight groups for the given source tree"""
    return query(_highlights.read_text(), tree.root_node)
