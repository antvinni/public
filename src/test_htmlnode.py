import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        child = HTMLNode("h", "child value text", children = None, props={"href": "https://www.google.com"})
        node = HTMLNode("p", "value text", child)
        node2 = HTMLNode("p", "value text", child)
        self.assertEqual(node, node2)
    
    def test_props_to_html(self):
        # Create a node with properties
        node = HTMLNode("a", "Link", props={"href": "https://example.com", "target": "_blank"})

        # Expected output for the props_to_html method
        expected_html = ' href="https://example.com" target="_blank"'

        # Assert that the output of props_to_html matches the expected string
        self.assertEqual(node.props_to_html(), expected_html)

    def test_repr(self):
        node = HTMLNode("a", "Link", props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(repr(node), f"HTMLNode({node.tag}, {node.value}, {node.children}, {node.props})")     

if __name__ == "__main__":
    unittest.main()
