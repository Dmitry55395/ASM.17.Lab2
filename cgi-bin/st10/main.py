from .shop import Shop

shop = Shop()

actions = {
    "show": shop.show,
    "show_insert_mobile_phone_form": shop.show_insert_mobile_phone_form,
    "show_insert_smart_phone_form": shop.show_insert_smart_phone_form,
    "show_edit_phone_form": shop.show_edit_phone_form,
    "clear": shop.clear,
    "insert_mobile_phone": shop.insert_mobile_phone,
    "insert_smart_phone": shop.insert_smart_phone,
    "delete_phone": shop.delete_phone,
    "edit_phone": shop.edit_phone
}


def main(q, self_url):
    action_name = q.getvalue('action', 'show')
    action = actions[action_name]
    print("Content-type: text/html; charset=utf-8\n\n")
    action(q, self_url)
