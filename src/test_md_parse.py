import unittest
from md_parse import split_nodes_delimiter
from textnode import TextType, TextNode

class TestMd_Parse(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_nodes_delimiter_bold(self):
        node = TextNode("normal blah blah **bold words** blah word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            [
                TextNode("normal blah blah ", TextType.TEXT),
                TextNode("bold words", TextType.BOLD),
                TextNode(" blah word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_nodes_delimiter_italic(self):
        node = TextNode("more plain text _italicized words_ meh meh", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            [
                TextNode("more plain text ", TextType.TEXT),
                TextNode("italicized words", TextType.ITALIC),
                TextNode(" meh meh", TextType.TEXT),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()