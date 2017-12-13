from .Native import Native
from .Foreign import Foreign
import pickle


class Music:
    musics = []
    FILE_PATH = 'cgi-bin/st41/data.dat'

    def __init__(self):
        self.init_from_file()

    @staticmethod
    def go_to_home_page(q, self_url):
        print('<meta http-equiv=refresh content="0; URL=' + self_url + '?student=' + q.getvalue('student') + '">')

    @staticmethod
    def show_insert_native_form(q, self_url):
        Native.show_add_form(q, self_url)

    @staticmethod
    def show_insert_foreign_form(q, self_url):
        Foreign.show_add_form(q, self_url)

    def show(self, q, self_url):
        print('<table border=1 align=center>')
        print('''
            <tr>
                <th width=50px>№</th>
                <th width=100px>Name</th>
                <th width=100px>Album name</th>
                <th width=100px>Year</th>
                <th width=100px>Country</th>
                <th width=100px></th>
            </tr>
        ''')
        id = 0
        for music in self.musics:
            id += 1
            print('''
                <tr>
                    <td align=center>{0}</td>                                
                    <td align=center>{1}</td>
                    <td align=center>{2}</td>
                    <td align=center>{3}</td>
                    <td align=center>{4}</td>
            '''.format(
                id,
                getattr(music, 'name', '') or '',
                getattr(music, 'album_name', '') or '',
                getattr(music, 'year', '') or '',
                getattr(music, 'country', '') or '',
            ))
            print('''
                <td>
                    <a href={0}?student={1}&id={2}&action={3}>редактировать</a>
                    <a href={0}?student={1}&id={2}&action={4}>удалить</a>
                </td>
            '''.format(
                self_url,
                q.getvalue('student'),
                id,
                'show_edit_form',
                'delete'
            ))
            print('</tr>')

        print('<tr>')
        print('<td colspan=6>')
        print("<a href={0}>назад</a>".format(self_url))
        print("<a href={0}?student={1}&action={2}>добавить отечественную</a>"
              .format(self_url, q.getvalue('student'), 'show_insert_native_form'))
        print("<a href={0}?student={1}&action={2}>добавить зарубежную</a>"
              .format(self_url, q.getvalue('student'), 'show_insert_foreign_form'))
        print("<a href={0}?student={1}&action={2}>очистить</a>"
              .format(self_url, q.getvalue('student'), 'clear'))
        print('</td>')
        print('</tr>')

        print('</table>')

    def show_edit_form(self, q, self_url):
        id = int(q.getvalue('id'))
        music = self.musics[id - 1]
        music.show_edit_form(q, self_url)

    def clear(self, q, self_url):
        self.musics.clear()
        self.save()
        self.go_to_home_page(q, self_url)

    def insert_native(self, q, self_url):
        music = Native(
            q.getvalue('name'),
            q.getvalue('album_name'),
            q.getvalue('year')
        )
        self.musics.append(music)
        self.save()
        self.go_to_home_page(q, self_url)

    def insert_foreign(self, q, self_url):
        music = Foreign(
            q.getvalue('name'),
            q.getvalue('album_name'),
            q.getvalue('year'),
            q.getvalue('country'),
        )
        self.musics.append(music)
        self.save()
        self.go_to_home_page(q, self_url)

    def delete(self, q, self_url):
        id = int(q.getvalue('id'))
        self.musics.pop(id - 1)
        self.save()
        self.go_to_home_page(q, self_url)

    def edit(self, q, self_url):
        id = int(q.getvalue('id'))
        music = self.musics[id - 1]
        music.edit(q)
        self.save()
        self.go_to_home_page(q, self_url)

    def init_from_file(self):
        file = open(self.FILE_PATH, 'rb')
        self.musics = pickle.load(file)
        file.close()

    def save(self):
        file = open(self.FILE_PATH, 'wb')
        pickle.dump(self.musics, file)
        file.close()
