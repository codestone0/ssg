import unittest

from textnode import TextNode, TextType


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
        

if __name__ == "__main__":
    unittest.main()