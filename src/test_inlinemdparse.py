import unittest
from inlinemdparse import (
    split_nodes_delimiter, extract_markdown_images, 
    extract_markdown_links, split_nodes_image,
    split_nodes_link
)
from textnode import TextType, TextNode

class Test_split_nodes_delimiter(unittest.TestCase):
    def test_code(self):
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

    def test_bold(self):
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

    def test_italic(self):
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

class Test_split_nodes_image(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) " \
            "and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

class Test_split_nodes_link(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) " \
            "and another [second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

class Test_extract_markdown_images(unittest.TestCase):
    def test_single(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_double(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)" \
        " and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        reference = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"), 
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
            ]
        matches = extract_markdown_images(text)
        self.assertListEqual(reference, matches)


class Test_extract_markdown_links(unittest.TestCase):
    def test_single(self):
        matches = extract_markdown_links(
            "Lorem ipsum dolor sit amet, consec[tetur](https://i.imgur.com/zjjcJKZ.png)adipiscing"
        )
        self.assertListEqual([("tetur", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_double(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)" \
        " and [to youtube](https://www.youtube.com/@bootdotdev)"
        reference = [
            ("to boot dev", "https://www.boot.dev"), 
            ("to youtube", "https://www.youtube.com/@bootdotdev")
            ]
        matches = extract_markdown_links(text)
        self.assertListEqual(reference, matches)

if __name__ == "__main__":
    unittest.main()