class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("To be implemented")

    def props_to_html(self):
        attributes = []
        if self.props == None:
            return ""

        for key in self.props:
            attributes.append(f" {key}={self.props[key]}")
        
        return ''.join(attributes)

    def __repr__(self):
        return f"TAG= {self.tag} VALUE= {self.value} CHILDREN={self.children} PROPS={self.props}"