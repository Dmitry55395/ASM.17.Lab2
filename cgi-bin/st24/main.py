from .CommunistParty import CommunistParty


def main(q, selfurl):
    print("Content-type: text/html; charset=utf-8\n\n")

    communist_party = CommunistParty(q, selfurl)

    menu = {
        "show_comrade_form": communist_party.show_comrade_form,
        "add_comrade": communist_party.add_comrade,
        "show_party_elite_form": communist_party.show_party_elite_form,
        "add_party_elite": communist_party.add_party_elite,
        "edit": communist_party.edit,
        "edit_in_party": communist_party.edit_in_party,
        "print_party_list": communist_party.print_party_list,
        "write_list_to_file": communist_party.write_to_file,
        "read_list_from_file": communist_party.read_from_file,
        "remove_comrade": communist_party.remove,
        "clear_list": communist_party.clear_party_list,
        "exit": None
    }

    communist_party.read_from_file()

    if 'action' in q:
        menu[q['action'].value]()
    else:
        menu['print_party_list']()
