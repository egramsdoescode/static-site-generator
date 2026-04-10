import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        expected_html = "<p>Hello, world!</p>"
        self.assertEqual(node.to_html(), expected_html)

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "google.com", {"href": "https://www.google.com"})
        expected_html = '<a href="https://www.google.com">google.com</a>'
        self.assertEqual(node.to_html(), expected_html)

    def test_leaf_to_html_span(self):
        node = LeafNode("span", "this is some text")
        expected_html = "<span>this is some text</span>"
        self.assertEqual(node.to_html(), expected_html)

    def test_leaf_to_html_value_error(self):
        node = LeafNode("span", "")
        with self.assertRaises(ValueError):
            node.to_html()
