from re import A
import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test__repr__(self):
        node = HTMLNode(
            "a",
            "test link",
            None,
            {"href": "https://www.google.com", "target": "_blank"},
        )
        expected_repr = """
tag:      a
value:    test link
children: None
props:    {'href': 'https://www.google.com', 'target': '_blank'}
        """

        self.assertEqual(repr(node), expected_repr)

    def test_to_html(self):
        node = HTMLNode(
            "a",
            "test link",
            None,
            {"href": "https://www.google.com", "target": "_blank"},
        )

        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            "test link",
            None,
            {"href": "https://www.google.com", "target": "_blank"},
        )
        expected_props = ' href="https://www.google.com" target="_blank"'

        self.assertEqual(node.props_to_html(), expected_props)
