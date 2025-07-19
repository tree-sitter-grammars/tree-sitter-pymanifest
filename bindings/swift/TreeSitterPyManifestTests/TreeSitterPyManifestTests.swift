import XCTest
import SwiftTreeSitter
import TreeSitterPyManifest

final class TreeSitterPyManifestTests: XCTestCase {
    func testCanLoadGrammar() throws {
        let parser = Parser()
        let language = Language(language: tree_sitter_pymanifest())
        XCTAssertNoThrow(try parser.setLanguage(language),
                         "Error loading PyPA manifest grammar")
    }
}
