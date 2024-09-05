from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props)
        self.attribute = self.props_to_html()

    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode requires a value")

        if self.tag == None or not self.tag.isalpha():
            return self.value
        elif self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}{self.attribute}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"<{self.tag}{self.attribute}>{self.value}</{self.tag}>"