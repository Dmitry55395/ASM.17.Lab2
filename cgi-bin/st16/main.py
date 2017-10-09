from .ContentManager import *


def main(q, self_url):
    print("Content-type: text/html; charset=utf-8\n\n")
    zoo = Zoo(q, self_url)
    ContentManager(zoo, self_url, q).show_content()
