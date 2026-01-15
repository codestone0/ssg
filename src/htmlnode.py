class HTMLNode:
    def __init__(self, 
                tag=None, 
                value=None, 
                children=None, 
                props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError('to_html not implemented')
    
    def props_to_html(self):
        if not self.props:
            return ""
        props_str = ""
        for item in self.props:
            props_str += f' {item}="{self.props[item]}"'
        return props_str
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, children: {self.children}, props: {self.props})'
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

        if not self.value:
            raise ValueError("value required for leaf nodes")
        
    def to_html(self):
        if not self.tag:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, props: {self.props})'
