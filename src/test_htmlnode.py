import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        child = HTMLNode("h", "child value text", children = None, props={"href": "https://www.google.com"})
        node = HTMLNode("p", "value text", child)
        node2 = HTMLNode("p", "value text", child)
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
