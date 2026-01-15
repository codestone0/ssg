import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_none(self):
        no_node = TextNode('This is not a URL', TextType.ITALIC)
        self.assertIsNone(no_node.url)
        yes_node = TextNode('This is a URL', TextType.LINK, 'https://127.0.0.1')
        self.assertEqual(yes_node.url, 'https://127.0.0.1')

    def test_noteq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
        
class Test_text_node_to_html_node(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "This is a text node")

    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, "This is a text node")

    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("This is a text node", TextType.LINK, 'https://altavista.digital.com')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.props['href'], node.url)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is a image node", TextType.IMAGE, 'https://127.0.0.1/image.jpg')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.props['src'], node.url)
        self.assertEqual(html_node.props['alt'], node.text)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, '')


if __name__ == "__main__":
    unittest.main()