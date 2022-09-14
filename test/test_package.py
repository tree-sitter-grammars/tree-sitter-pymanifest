#!/usr/bin/env python3

import unittest as test

import tree_sitter_pymanifest as pymf

class TestPackage(test.TestCase):
    def setUp(self) -> None:
        self.source = b'recursive-include tests *'
        self.tree = pymf.parse(self.source)

    def test_parse(self):
        nodes = self.tree.root_node.named_children
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].type, 'command')
        self.assertEqual(nodes[0].text, self.source)

    def test_query(self):
        query = '(command dir_pattern: (pattern) @dir)'
        captures = pymf.query(query, self.tree.root_node)
        self.assertEqual(len(captures), 1)
        self.assertEqual(captures[0][1], 'dir')
        self.assertEqual(captures[0][0].text, b'tests')

    def test_highlights(self):
        captures = pymf.highlights(self.tree)
        self.assertEqual(len(captures), 2)
        self.assertEqual(captures[0][1], 'keyword')
        self.assertEqual(captures[0][0].type, 'keyword')
        self.assertEqual(captures[1][1], 'punctuation.special')
        self.assertEqual(captures[1][0].type, 'glob')

if __name__ == '__main__':
    test.main(verbosity=2)
