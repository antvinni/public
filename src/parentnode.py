from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Invalid HTML: no tag value in parent node")
        if not self.children:
            raise ValueError("Invalid HTML: no children in parent node")
        html_string = ""
        for child in self.children:
            html_string += child.to_html()
            print(child.to_html())
        return f'<{self.tag}>{html_string}</{self.tag}>' 
