import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(
            TextNode("This is a text node", TextType.BOLD_TEXT),
            TextNode("This is a text node", TextType.BOLD_TEXT),
        )


if __name__ == "__main__":
    unittest.main()
