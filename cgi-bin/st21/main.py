from .prison import *


def main(f_param, self_url):
    print("Content-type: text/html; charset=utf-8\n\n")
    prison = Prison(f_param, self_url)
    actions_list = {
        'print_data': prison.print_data,
        'get_data': prison.get_data,
        'add_prisoner': prison.add_prisoner,
        'add_overseer': prison.add_overseer,
        'edit_stack': prison.edit_stack,
        'delete_person': prison.remove_person,
        'clear_list': prison.clear_list
    }
    if 'action' in f_param:
        actions_list[f_param.getvalue('action')]()
    else:
        actions_list['print_data']()

