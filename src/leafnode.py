from htmlnode import HTMLNode
from typing import Optional, Dict


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str | None,
        value: str,
        props: Optional[Dict[str, str]] = None,
    ) -> None:
        super().__init__(tag, value, None, props)

    def __repr__(self) -> str:
        return f"""
tag:      {self.tag}
value:    {self.value}
props:    {self.props}
        """

    def to_html(self) -> str | ValueError:
        if not self.value:
            raise ValueError("Leaf nodes must have a value")
        return (
            f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
            if self.tag
            else self.value
        )
