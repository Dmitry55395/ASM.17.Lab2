from .ContentManager import * 


def main(q, self_url):
    print("Content-type: text/html; charset=utf-8\n\n")
    stores = Stores(q, self_url)
    ContentManager(stores, self_url, q).show_content()
