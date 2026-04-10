import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def setUp(self):
        self.node = HTMLNode(
            "a",
            "test link",
            None,
            {"href": "https://www.google.com", "target": "_blank"},
        )

    def test_repr(self):
        expected = (
            "\ntag:      a\n"
            "value:    test link\n"
            "children: None\n"
            "props:    {'href': 'https://www.google.com', 'target': '_blank'}\n"
            "        "
        )
        self.assertEqual(repr(self.node), expected)

    def test_to_html(self):
        with self.assertRaises(NotImplementedError):
            self.node.to_html()

    def test_props_to_html(self):
        expected_props = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(self.node.props_to_html(), expected_props)
