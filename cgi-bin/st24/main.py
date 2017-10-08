from .catalog import *

def main(q, selfurl):
    catalog = Catalog(q,selfurl)
    catalog.load()
    MENU = {
        'show': catalog.show,
        'get':catalog.get,
        'addnew':catalog.add_new,
        'addused':catalog.add_used,
        'edit':catalog.edit_catalog,
        'delete':catalog.delete_auto,
        'clear':catalog.clear_catalog
    }
    print ("Content-type: text/html; charset=utf-8\n\n")
    if 'act' in q:
        MENU[q.getvalue('act')]()
    else:
        MENU['show']()

    catalog.save()
