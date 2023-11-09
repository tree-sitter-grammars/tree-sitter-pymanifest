======================
tree-sitter-pymanifest
======================

.. image:: https://badgen.net/github/checks/ObserverOfTime/tree-sitter-pymanifest?label=CI&icon=github
   :target: https://github.com/ObserverOfTime/tree-sitter-pymanifest/actions/workflows/ci.yml
   :alt: CI

A tree-sitter parser for PyPA manifest files.

Python package
--------------

Installation
^^^^^^^^^^^^

.. code-block:: bash

   pip install tree-sitter-pymanifest

Usage
^^^^^

.. code-block:: python

   import tree_sitter_pymanifest as pymanifest

   with open('MANIFEST.in', 'r') as mf:
      # parse a MANIFEST.in file
      tree = pymanifest.parse(mf.read())
      # get the highlight groups
      hl_groups = pymanifest.highlights(tree)
      # run an arbitrary query
      dir_patterns = pymanifest.query("""
      (command dir_pattern: (pattern) @dir_pattern)
      """, tree.root_node)


References
----------

* `MANIFEST.in commands <https://packaging.python.org/en/latest/guides/using-manifest-in/#manifest-in-commands>`_
* `Unix filename pattern matching <https://docs.python.org/3/library/fnmatch.html>`_

Editors
-------

| |c| Neovim
| |u| Helix
| |u| Emacs

.. |u| unicode:: U+00A0 U+00A0 U+2610
.. |c| unicode:: U+00A0 U+00A0 U+2611


Changelog
---------

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
