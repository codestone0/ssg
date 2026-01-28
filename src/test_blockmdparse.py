import unittest

from blockmdparse import markdown_to_blocks, BlockType, block_to_block_type

class Test_markdown_to_blocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md ="""
This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items
"""

        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                'This is **bolded** paragraph',
                'This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line',
                '- This is a list\n- with items'
            ]
        )

class Test_block_to_block_type(unittest.TestCase):
    def test_block_to_type(self):
        p_block = "sd drfawsd fafasdf aergf asdc " \
                  "asdfsdrtg asdvqwef asxzc asrg asdcv awergf " \
                  "tyujn cjnuyb987y kjhn98awe fkjnikjunaewrf 8"
        h1_block = "# Lookit that big ol heading."
        h6_block = "###### So tiny"
        code_block = "```\n" \
                     "spaghetti code ( 5 ? 'heads' : 'tails' )\n" \
                     "def pizza_me():\n" \
                     "bool `javascript string`\n" \
                     "```"
        quote_block = "> There is no try\n" \
                      ">only do."
        ul_block = "- some stuff\n" \
                   "- eggs\n" \
                   "- donuts"
        ol_block = "1. one, two\n" \
                   "2. cows go moo\n" \
                   "3. three, four\n" \
                   "4. I lost the door"

        self.assertEqual(block_to_block_type(p_block), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(h1_block), BlockType.HEADING)
        self.assertEqual(block_to_block_type(h6_block), BlockType.HEADING)
        self.assertEqual(block_to_block_type(code_block), BlockType.CODE)
        self.assertEqual(block_to_block_type(quote_block), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(ul_block), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type(ol_block), BlockType.ORDERED_LIST)
        