from .Container import *


def main(q, selfurl):
    print("Content-type: text/html; charset=utf-8\n\n")
    container = Container(q, selfurl)
    content = {
        'show_menu': container.show_menu,
        'show_edit_card': container.show_edit_card,
        'save_personal_card': container.save_personal_card,
        'delete_personal_card': container.delete_personal_card,
        'clear_container': container.clear_container
    }

    if 'action' in q:
        content[q['action'].value]()
    else:
        content['show_menu']()

    if __name__ == "__main__":
            main()