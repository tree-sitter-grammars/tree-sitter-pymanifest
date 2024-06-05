======================
tree-sitter-pymanifest
======================

|CI| |discord| |matrix| |pypi|

A tree-sitter parser for PyPA manifest files.

Python package
--------------

Installation
^^^^^^^^^^^^

.. code-block:: bash

   pip install tree-sitter-pymanifest


References
----------

* `Controlling files in the distribution <https://setuptools.pypa.io/en/latest/userguide/miscellaneous.html>`_
* `Unix filename pattern matching <https://docs.python.org/3/library/fnmatch.html>`_

Editors
-------

| |c| Neovim
| |u| Helix
| |u| Emacs
| |u| Zed

.. |u| unicode:: U+00A0 U+00A0 U+2610
.. |c| unicode:: U+00A0 U+00A0 U+2611


Changelog
---------

v0.5.1
^^^^^^

* Fix package description

v0.5.0
^^^^^^

* Update bindings
* Remove custom functions
* Drop Python 3.8 support

v0.4.0
^^^^^^

* Change bindings layout

v0.3.0
^^^^^^

* Move to ``tree-sitter-grammars`` org

v0.2.1
^^^^^^

* Drop Python 3.7 support
* Remove injections queries
* Use tree-sitter core highlight captures

v0.2.0
^^^^^^

* Add Python package tests

v0.1.1
^^^^^^

* Bundle queries in the package

.. |CI| image:: https://img.shields.io/github/actions/workflow/status/tree-sitter-grammars/tree-sitter-pymanifest/test.yml?logo=github&label=CI
   :target: https://github.com/tree-sitter-grammars/tree-sitter-pymanifest/actions/workflows/test.yml
   :alt: CI

.. |discord| image:: https://img.shields.io/discord/1063097320771698699?logo=discord&label=discord
   :target: https://discord.gg/w7nTvsVJhm
   :alt: discord

.. |matrix| image:: https://img.shields.io/matrix/tree-sitter-chat%3Amatrix.org?logo=matrix&label=matrix
   :target: https://matrix.to/#/#tree-sitter-chat:matrix.org
   :alt: matrix

.. |pypi| image:: https://img.shields.io/pypi/v/tree-sitter-pymanifest?logo=pypi&logoColor=ffd242
   :target: https://pypi.org/project/tree-sitter-pymanifest/
   :alt: pypi
