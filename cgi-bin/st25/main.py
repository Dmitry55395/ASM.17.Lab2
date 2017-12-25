from .group import *


def main(q, self_url):
    print("Content-type: text/html; charset=utf-8\n\n")
    container = Container(q, self_url)
    Group(container, self_url, q).show_content()
