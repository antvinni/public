

from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode


def main():
    TN = TextNode("text", "bold", "google.com")
    print(repr(TN))   
main()