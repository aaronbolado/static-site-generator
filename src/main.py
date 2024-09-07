from textnode import TextNode
from htmlnode import *

def main():
    print("running main.py")
    textnode = TextNode("This is a text node", "bold", "https://www.boot.dev")
    node = HTMLNode("tag", "this is a value", 
                        "this is a child", 
                        {"href":"www.youtube.com",
                        "target": "__blank"})
    print(textnode)
    print(node)
    new_html = text_node_to_html_node(textnode).to_html()
    print(new_html)

def text_node_to_html_node(text_node):
    text_types = ["text", "bold", "italic",
                    "code", "link", "image"]
    if text_node.text_type not in text_types:
        raise ValueError("Invlaid text_type: does not exist")

    if text_node.text_type == "text":
        return LeafNode(None, text_node.text)
    elif text_node.text_type == "bold":
        return LeafNode("b", text_node.text)
    elif text_node.text_type == "italic":
        return LeafNode("i", text_node.text)
    elif text_node.text_type == "code":
        return LeafNode("code", text_node.text)
    elif text_node.text_type == "link":
        return LeafNode("a", text_node.text, {"href":text_node.url})
    elif text_node.text_type == "image":
        return LeafNode("img", None, {"src":text_node.url, "alt": text_node.text})

main()