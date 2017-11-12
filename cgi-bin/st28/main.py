from .ModelAgency import ModelAgency


def main(q, selfurl):
    agency = ModelAgency(q, selfurl)
    menu = {
            "show_agency_and_menu": agency.show_agency_and_menu,
            "show_edit": agency.show_model_edit,
            "save_model": agency.save_model,
            "remove_model": agency.remove_model,
            "clear_agency": agency.clear_agency
    }
    print("Content-type: text/html; charset=utf-8\n\n")

    if 'action' in q:
        menu[q['action'].value]()
    else:
        menu['show_agency_and_menu']()

