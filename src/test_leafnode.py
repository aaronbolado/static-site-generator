import unittest

from htmlnode import *
from textnode import *

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
        textnode2 = TextNode("This is a text node", "image", "https://www.boot.dev")
        textnode3 = TextNode("This is a text node", "link", "https://www.boot.dev")
        node = HTMLNode("tag", "this is a value", 
                            "this is a child", 
                            {"href":"www.youtube.com",
                            "target": "__blank"})
        print(textnode)
        print(node)
        new_html = text_node_to_html_node(textnode).to_html()
        new_html2 = text_node_to_html_node(textnode2).to_html()
        new_html3 = text_node_to_html_node(textnode3).to_html()
        print(new_html)
        print(new_html2)
        print(new_html3)

if __name__ == "__main__":
    unittest.main()