import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test(self):
        node = HTMLNode("tag", "this is a value", 
                        "this is a child", 
                        {"href":"www.youtube.com",
                        "target": "__blank"})
        print(node.props_to_html())
    
    def test(self):
        node = HTMLNode("tag", None, 
                        "this is a child", 
                        None)
        print(node.props_to_html())
    
    def test(self):
        node = HTMLNode()
        print(node.props_to_html())

if __name__ == "__main__":
    unittest.main()