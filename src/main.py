from textnode import TextNode, TextType


def main():
    print(
        TextNode("This is some anchor text", TextType.ANCHOR_TEXT, "https://boot.dev")
    )


main()
