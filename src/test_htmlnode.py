import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "a", 
            "forgotten bones", 
            [], 
            {'href':'http://www.dec.com','target':'_self'}
        )
        self.assertEqual(
            node.props_to_html(), 
            ' href="http://www.dec.com" target="_self"'
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "the story isn't over yet"
        )
        self.assertEqual(node.tag, 'div')
        self.assertEqual(node.value, "the story isn't over yet")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_repr(self):
        node = HTMLNode(
            "p",
            "hope is...",
            None,
            {'class': 'alpha'}
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, hope is..., children: None, props: {'class': 'alpha'})"
        )


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Learn here!", {"href": "https://www.boot.dev"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.boot.dev">Learn here!</a>'
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Trogdor!!")
        self.assertEqual(node.to_html(), "Trogdor!!")
        

class TestParentNode(unittest.TestCase):
    def test_parent_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

        
if __name__ == "__main__":
    unittest.main()