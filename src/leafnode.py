from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag = None, props = None) -> None:
        super().__init__(value = value, tag = tag, children= None, props = props)
    
    def to_html(self):
        
        if not self.value:
            raise ValueError
        
        if self.tag == None:
            return str(self.value)
        if self.props == None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'