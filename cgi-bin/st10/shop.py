from .MobilePhone import MobilePhone
from .SmartPhone import SmartPhone
import pickle


class Shop:
    shop = []
    FILE_PATH = 'cgi-bin/st10/mobile_phone_shop.dat'

    def __init__(self):
        self.init_from_file()

    @staticmethod
    def go_to_home_page(q, self_url):
        print('<meta http-equiv=refresh content="0; URL=' + self_url + '?student=' + q.getvalue('student') + '">')

    @staticmethod
    def show_insert_mobile_phone_form(q, self_url):
        MobilePhone.show_add_form(q, self_url)

    @staticmethod
    def show_insert_smart_phone_form(q, self_url):
        SmartPhone.show_add_form(q, self_url)

    def show(self, q, self_url):
        print("<a href={0}>назад</a>".format(self_url))
        print("<a href={0}?student={1}&action={2}>добавить телефон</a>"
              .format(self_url, q.getvalue('student'), 'show_insert_mobile_phone_form'))
        print("<a href={0}?student={1}&action={2}>добавить смартфон</a>"
              .format(self_url, q.getvalue('student'), 'show_insert_smart_phone_form'))
        print("<a href={0}?student={1}&action={2}>очистить</a>"
              .format(self_url, q.getvalue('student'), 'clear'))
        print('<table border=1 cellspacing=0 cellpadding=7>')
        print('''
            <tr bgcolor=#ffffb3>
                <th width=50px>№</th>
                <th width=100px>Brand</th>
                <th width=100px>Screen size</th>
                <th width=100px>Housing type</th>
                <th width=100px>OS</th>
                <th width=100px>RAM</th>
                <th width=100px></th>
            </tr>
        ''')
        id = 0
        for mobile in self.shop:
            id += 1
            print('''
                <tr bgcolor={0}>
                    <td align=center>{1}</td>                                
                    <td align=center>{2}</td>
                    <td align=center>{3}</td>
                    <td align=center>{4}</td>
                    <td align=center>{5}</td>
                    <td align=center>{6}</td>
            '''.format(
                mobile.get_color(),
                id,
                getattr(mobile, 'brand', '') or '',
                getattr(mobile, 'screen_size', '') or '',
                getattr(mobile, 'housing_type', '') or '',
                getattr(mobile, 'os', '') or '',
                getattr(mobile, 'ram', '') or ''
            ))
            print('''
                <td>
                    <a href={0}?student={1}&id={2}&action={3}>Редактировать</a>
                    <a href={0}?student={1}&id={2}&action={4}>Удалить</a>
                </td>
            '''.format(
                self_url,
                q.getvalue('student'),
                id,
                'show_edit_phone_form',
                'delete_phone'
            ))
            print('</tr>')
        print('</table>')

    def show_edit_phone_form(self, q, self_url):
        id = int(q.getvalue('id'))
        phone = self.shop[id - 1]
        phone.show_edit_form(q, self_url)

    def clear(self, q, self_url):
        self.shop.clear()
        self.save()
        self.go_to_home_page(q, self_url)

    def insert_mobile_phone(self, q, self_url):
        mobile_phone = MobilePhone(
            q.getvalue('brand'),
            q.getvalue('screen_size'),
            q.getvalue('housing_type')
        )
        self.shop.append(mobile_phone)
        self.save()
        self.go_to_home_page(q, self_url)

    def insert_smart_phone(self, q, self_url):
        smart_phone = SmartPhone(
            q.getvalue('brand'),
            q.getvalue('screen_size'),
            q.getvalue('housing_type'),
            q.getvalue('os'),
            q.getvalue('ram')
        )
        self.shop.append(smart_phone)
        self.save()
        self.go_to_home_page(q, self_url)

    def delete_phone(self, q, self_url):
        id = int(q.getvalue('id'))
        self.shop.pop(id - 1)
        self.save()
        self.go_to_home_page(q, self_url)

    def edit_phone(self, q, self_url):
        id = int(q.getvalue('id'))
        phone = self.shop[id - 1]
        phone.edit(q)
        self.save()
        self.go_to_home_page(q, self_url)

    def init_from_file(self):
        file = open(self.FILE_PATH, 'rb')
        self.shop = pickle.load(file)
        file.close()

    def save(self):
        file = open(self.FILE_PATH, 'wb')
        pickle.dump(self.shop, file)
        file.close()
