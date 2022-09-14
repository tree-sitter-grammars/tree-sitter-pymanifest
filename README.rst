======================
tree-sitter-pymanifest
======================

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

   with open('MANIFEST.in', 'rb') as mf:
      # parse a MANIFEST.in file
      tree = pymanifest.parse(mf.read())
      # get the highlight groups
      hl_groups = pymanifest.highlights(tree.root_node)
      # run an arbitrary query
      dir_patterns = pymanifest.query("""
      ((command dir_pattern: (pattern) @dir_pattern))
      """).captures(tree.root_node)
