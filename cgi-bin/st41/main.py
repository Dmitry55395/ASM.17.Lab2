from .Music import Music

music = Music()

actions = {
    "show": music.show,
    "show_insert_native_form": music.show_insert_native_form,
    "show_insert_foreign_form": music.show_insert_foreign_form,
    "show_edit_form": music.show_edit_form,
    "clear": music.clear,
    "insert_native": music.insert_native,
    "insert_foreign": music.insert_foreign,
    "delete": music.delete,
    "edit": music.edit
}


def main(q, self_url):
    action_name = q.getvalue('action', 'show')
    action = actions[action_name]
    print("Content-type: text/html; charset=utf-8\n\n")
    action(q, self_url)
