import re

block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ul = "unordered list"
block_type_ol = "ordered list"
block_type_p = "normal paragraph"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    # Assumes block contains \n characters
    lines = block.split("\n")

    # looks for single heading with 1 to 6 '#' sign
    if re.search(r"^#{1,6} (.*?)", block):
        return block_type_heading
    
    # looks for ``` code ``` syntax which includes newlines
    if re.search(r"^```((.|\n)*?)```", block):
        return block_type_code
    
    # looks for quotes from multiple lines
    if block.startswith("> "):
        for line in lines:
            if not line.startswith("> "):
                return block_type_p
        return block_type_quote
    
    # looks for unordered lists starting with * or - from multiple lines
    if re.match(r"(\*|-) ", block):
        for line in lines:
            if not re.match(r"(\*|-) ", line):
                return block_type_p
        return block_type_ul
    
    # looks for ordered lists starting with 1. incrementing
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_p
            i += 1
        return block_type_ol

    return block_type_p