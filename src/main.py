from textnode import TextNode, TextType
from htmlnode import HTMLNode


def main():
    print(
        TextNode("This is some anchor text", TextType.ANCHOR_TEXT, "https://boot.dev")
    )

    props = {"href": "https://www.google.com", "target": "_blank"}
    html = HTMLNode(None, None, None, props)

    print(html)


main()
