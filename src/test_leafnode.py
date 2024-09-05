import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test(self):
        node = LeafNode("This is a paragraph of text.","p")
        node2 = LeafNode("Click me!", "a", {"href": "https://www.google.com"})
    
    def test(self):
        node = LeafNode("This is a paragraph of text.")
        node2 = LeafNode("Click me!", None, {"href": "https://www.google.com", "href": "https://youtube.com"})
    
    def test(self):
        node = LeafNode("","p")
        node2 = LeafNode("asdad", " ", {"href": "https://www.google.com"})
        node3 = LeafNode("aaaaa", " ", None)

        print("TEST 3")
        print(node.to_html())
        print("TEST 3")
        print(node2.to_html())
        print("TEST 3")
        print(node3.to_html())

if __name__ == "__main__":
    unittest.main()