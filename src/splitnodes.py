import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

IMG_REGEX = r"!\[(.*?)\]\((.*?)\)"       # Gets pattern ![alt](url)
LINK_REGEX = r"(?<!!)\[(.*?)\]\((.*?)\)" # Gets pattern [alt](url)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:

        # If current node isn't text type, we append and ignore it (no reason to split an non-text type)
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        split_nodes = []

        # If there are no images in text, we append and proceed to next iteration
        if len(images) == 0:
            new_nodes.append(old_node)
            continue

        for image in images:
            # splits current text into two sections
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")

            # split can return "" for one side of the delimiter if there are no text 
            # (image is found at the beginning or end of the text) 
            if sections[0] != "":
                # append text node of type text if the beginning of the text is not an image/empty    
                new_nodes.append(TextNode(sections[0], text_type_text))
            
            # append image to new nodes if it's in the beginning of the text
            new_nodes.append(TextNode(image[0], text_type_image, image[1]))
            
            # gives the second half of the original text to the next iteration
            original_text = sections[1]
        
        # If the end of the text isn't empty, append it to the new node list
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes

def extract_markdown_images(text):
    tuple_list = []
    alt_url_list = re.findall(IMG_REGEX, text)
    
    for i in range(len(alt_url_list)):
        if len(alt_url_list[i]) % 2 != 0:
            raise ValueError("Invalid image: missing alt or url")
        
        alt = alt_url_list[i][0]
        url = alt_url_list[i][1]
        
        tuple_list.append((alt, url))

    return tuple_list

def extract_markdown_links(text):
    tuple_list = []
    alt_url_list = re.findall(LINK_REGEX, text)
    for i in range(len(alt_url_list)):
        if len(alt_url_list[i]) % 2 != 0:
            raise ValueError("Invalid link: missing alt or url")
        
        alt = alt_url_list[i][0]
        url = alt_url_list[i][1]

        tuple_list.append((alt, url))
    
    return tuple_list

def text_to_textnodes(text):
    new_nodes = split_nodes_delimiter([TextNode(text, text_type_text)], "**", text_type_bold)
    new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
    new_nodes = split_nodes_delimiter(new_nodes, "`", text_type_code)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)

    return new_nodes
