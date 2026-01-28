import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    for i in range(len(blocks)):
        blocks[i] = blocks[i].strip()
    return [block for block in blocks if len(block)]

def block_to_block_type(block):
    if re.fullmatch(r"^#{1,6} [\w\d\s\.]+", block):
        return BlockType.HEADING
    if re.fullmatch(r"^```([\S]*)?\n[[\s\S]+\n]*\```$", block):
        return BlockType.CODE
    if re.fullmatch(r"((>)(.{1,}\n?))+", block):
        return BlockType.QUOTE
    if re.fullmatch(r"((-)( {1,})(.{1,}\n?))+", block):
        return BlockType.UNORDERED_LIST
    if re.fullmatch(r"(([0-9]{1,})\. (.{1,}\n?))+", block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH