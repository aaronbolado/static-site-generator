import unittest
from markdown_blocks import *


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_block_to_heading(self):
        block = "###### This is code ```"
        print(f"Heading: {block[:3]} end")
        print(f"End: {block[len(block)-1:len(block)-4:-1]} end")
        block_type = block_to_block_type(block)
        print(f"Block Type: {block_type}")
        self.assertEqual(
            block_type,
            "heading",
        )

    def test_block_to_code(self):
        block = "``` \nThis is code \n```"
        print(f"Code: {block[:3]} end")
        print(f"End: {block[len(block)-1:len(block)-4:-1]} end")
        block_type = block_to_block_type(block)
        print(f"Block Type: {block_type}")
        self.assertEqual(
            block_type,
            "code",
        )

    def test_block_to_quote(self):
        block = "> quote\n> more quote"
        print(f"Quote: {block[:3]} end")
        print(f"End: {block[len(block)-1:len(block)-4:-1]} end")
        block_type = block_to_block_type(block)
        print(f"Block Type: {block_type}")
        self.assertEqual(
            block_type,
            "quote",
        )

    def test_block_to_ul(self):
        block = "* list\n- items"
        print(f"UL: {block[:3]} end")
        print(f"End: {block[len(block)-1:len(block)-4:-1]} end")
        block_type = block_to_block_type(block)
        print(f"Block Type: {block_type}")
        self.assertEqual(
            block_type,
            "unordered list",
        )
        
        block = "- This is unordered list ```"
        print(f"UL: {block[:3]} end")
        block_type = block_to_block_type(block)
        print(f"Block Type: {block_type}")
        self.assertEqual(
            block_type,
            "unordered list",
        )

    def test_block_to_ol(self):
        block = "1. list\n2. items"
        print(f"OL: {block[:3]} end")
        print(f"End: {block[len(block)-1:len(block)-4:-1]} end")
        block_type = block_to_block_type(block)
        print(f"Block Type: {block_type}")
        self.assertEqual(
            block_type,
            "ordered list",
        )
        
        block = "2. This \n4. is not an ordered list ```"
        print(f"OL: {block[:3]} end")
        block_type = block_to_block_type(block)
        print(f"Block Type: {block_type}")
        self.assertEqual(
            block_type,
            "normal paragraph",
        )

    def test_block_to_normal_paragraph(self):
        block = "#> This ``` is # code ```"
        print(f"NP: {block[:3]} end")
        print(f"End: {block[len(block)-1:len(block)-4:-1]} end")
        block_type = block_to_block_type(block)
        print(f"Block Type: {block_type}")
        self.assertEqual(
            block_type,
            "normal paragraph",
        )

if __name__ == "__main__":
    unittest.main()
