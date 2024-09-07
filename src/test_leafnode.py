import unittest

from htmlnode import *
from main import text_node_to_html_node
from textnode import TextNode

class TestLeafNode(unittest.TestCase):
    def test_leafnode_sample(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    
    def test_leafnode_empty(self):
        node = LeafNode("","This is a paragraph of text.")
        node2 = LeafNode(None, "Click me!", {"href": "https://www.google.com", "href": "https://youtube.com"})
    
    def test_leafnode_none(self):
        node = LeafNode("p", "")
        node2 = LeafNode(" ", "asdad", {"href": "https://www.google.com"})
        node3 = LeafNode("ko", "aaaaa", None)
    
    def test_text_to_html(self):
        textnode = TextNode("This is a text node", "bold", "https://www.boot.dev")
        # textnode2 = TextNode("", "ascii", "https://www.boot.dev")
        # textnode3 = TextNode("", "img", "image_url")
        # print(text_node_to_html_node(textnode2))
        # print(text_node_to_html_node(textnode3))

if __name__ == "__main__":
    unittest.main()