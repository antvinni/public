import unittest

from textnode import TextNode
from leafnode import LeafNode
from text_node_to_html import text_node_to_html_node

class Test_text_node_to_html(unittest.TestCase):
    def test_text_node_to_html(self):
        tn = TextNode("This is a text node", "bold")
        self.assertEqual(text_node_to_html_node(tn), LeafNode('b','This is a text node', None))

if __name__ == "__main__":
    unittest.main()