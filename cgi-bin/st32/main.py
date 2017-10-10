from .Menu import Menu

def main(q, selfurl):
    print("Content-type: text/html; charset=utf-8\n\n")
    menu = Menu(q, selfurl)
    if 'act' not in q:
        menu.index()
    else:
        menu.act()
        