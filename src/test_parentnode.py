import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_parent(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(), 
            '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        )
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode("a", "Normal text", {"key1":"value1", "key2":"value2"}),
            ],
        )
        self.assertEqual(
            node.to_html(), 
            '<p><b>Bold text</b>Normal text<i>italic text</i><a key1="value1" key2="value2">Normal text</a></p>'
        )

if __name__ == "__main__":
    unittest.main()