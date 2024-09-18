class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other: object) -> bool:
        # Ensure 'other' is an HTMLNode instance
        if not isinstance(other, HTMLNode):
            return False
        
        # Compare tag, value, attributes, and children
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html_string = ""
        for key, value in self.props.items():
            html_string += f" {key} {value}"
        return html_string
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.childrent}, {self.props})"
    