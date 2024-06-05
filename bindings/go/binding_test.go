package tree_sitter_pymanifest_test

import (
	"testing"

	tree_sitter "github.com/smacker/go-tree-sitter"
	"github.com/tree-sitter-grammars/tree-sitter-pymanifest"
)

func TestCanLoadGrammar(t *testing.T) {
	language := tree_sitter.NewLanguage(tree_sitter_pymanifest.Language())
	if language == nil {
		t.Errorf("Error loading Pymanifest grammar")
	}
}
