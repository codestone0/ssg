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
        raise Exception(NotImplementedError)
    
    def props_to_html(self):
        if not self.props:
            return ""
        props_str = ""
        for item in self.props:
            props_str += f' {item}="{self.props[item]}"'
        return props_str
    
    def __repr__(self):
        return f'tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}'
    