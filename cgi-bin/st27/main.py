from .eLibrary import eLibrary

def main(q, selfurl):

    library = eLibrary(q, selfurl)
    
    menu = {
            "show_actions_menu": library.show_actions_menu,
            "show_form_add_sbornik": library.show_form_add_sbornik,
            "show_form_add_mest_sbornik": library.show_form_add_mest_sbornik,
            "save_sbornik": library.save_sbornik,
            "clear": library.clear_library,
            "remove_sbornik": library.remove_sbornik,
    }
    print("Content-type: text/html; charset=utf-8\n\n")

    if 'action' in q:
        menu[q['action'].value]()
    else:
        menu['show_actions_menu']()
