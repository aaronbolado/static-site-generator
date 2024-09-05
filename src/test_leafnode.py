import unittest

from htmlnode import *

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

if __name__ == "__main__":
    unittest.main()