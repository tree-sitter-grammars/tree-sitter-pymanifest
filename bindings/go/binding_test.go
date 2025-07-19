package tree_sitter_pymanifest_test

import (
	"testing"

	tree_sitter "github.com/tree-sitter/go-tree-sitter"
	tree_sitter_pymanifest "github.com/tree-sitter-grammars/tree-sitter-pymanifest/bindings/go"
)

func TestCanLoadGrammar(t *testing.T) {
	language := tree_sitter.NewLanguage(tree_sitter_pymanifest.Language())
	if language == nil {
		t.Errorf("Error loading PyPA manifest grammar")
	}
}
