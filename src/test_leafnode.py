import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    
    def test_leafnode_initialization(self):
        # Test with tag, value, and props
        node = LeafNode(value="Content", tag="p", props={"class": "text-bold"})
        self.assertEqual(node.value, "Content")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.props, {"class": "text-bold"})
        self.assertEqual(node.children, None)  # Leaf nodes should have no children

    def test_leafnode_initialization_no_tag(self):
        # Test with value but no tag
        node = LeafNode(value="Content")
        self.assertEqual(node.value, "Content")
        self.assertIsNone(node.tag)
        self.assertEqual(node.props, None)
    
    def test_leafnode_to_html_with_tag(self):
        # Test that to_html works when a tag is provided
        node = LeafNode(value="Content", tag="p", props={"class": "text-bold"})
        self.assertEqual(node.to_html(), '<p class="text-bold">Content</p>')

    def test_leafnode_to_html_no_tag(self):
        # Test that to_html works when no tag is provided (returns just the value)
        node = LeafNode(value="Plain text")
        self.assertEqual(node.to_html(), "Plain text")

    def test_leafnode_to_html_empty_value(self):
        # Test that to_html raises ValueError when value is None
        with self.assertRaises(ValueError):
            node = LeafNode(value=None)
            node.to_html()

        # Test that to_html raises ValueError when value is an empty string
        with self.assertRaises(ValueError):
            node = LeafNode(value="")
            node.to_html()
        
    def test_leafnode_repr(self):
        # Test the repr output with tag, value, and props
        node = LeafNode(value="Content", tag="p", props={"class": "text-bold"})
        expected_repr = "LeafNode(p, Content, {'class': 'text-bold'})"
        self.assertEqual(repr(node), expected_repr)

        # Test the repr output with no tag and no props
        node_no_tag = LeafNode(value="Plain text")
        expected_repr_no_tag = "LeafNode(None, Plain text, None)"
        self.assertEqual(repr(node_no_tag), expected_repr_no_tag)

if __name__ == "__main__":
    unittest.main()
