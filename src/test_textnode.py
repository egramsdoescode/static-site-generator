import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(
            TextNode("This is a text node", TextType.BOLD_TEXT),
            TextNode("This is a text node", TextType.BOLD_TEXT),
        )

    def test_not_eq(self):
        self.assertNotEqual(
            TextNode("This is a text node", TextType.BOLD_TEXT),
            TextNode("This is a text node", TextType.PLAIN_TEXT),
        )

    def test_url(self):
        self.assertEqual(
            TextNode("This is a test node", TextType.ANCHOR_TEXT, "https://google.com"),
            TextNode("This is a test node", TextType.ANCHOR_TEXT, "https://google.com"),
        )

    def test_no_url(self):
        self.assertNotEqual(
            TextNode("This is a test node", TextType.ANCHOR_TEXT, "https://google.com"),
            TextNode("This is a test node", TextType.ANCHOR_TEXT, None),
        )


if __name__ == "__main__":
    unittest.main()
