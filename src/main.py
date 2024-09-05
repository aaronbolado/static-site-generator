from textnode import TextNode
from htmlnode import HTMLNode

def main():
    print("running main.py")
    textnode = TextNode("This is a text node", "bold", "https://www.boot.dev")
    node = HTMLNode("tag", "this is a value", 
                        "this is a child", 
                        {"href":"www.youtube.com",
                        "target": "__blank"})
    print(textnode)
    print(node)

main()