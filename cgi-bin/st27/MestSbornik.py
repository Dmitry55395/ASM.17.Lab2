from .Sbornik import Sbornik

class MestSbornik(Sbornik):

    def __init__(self, name, developer, date, organization):
        self.name = name
        self.developer = developer
        self.date = date
        self.organization = organization

    def show_sbornik(self, q, self_number):
        student_id = q['student'].value
        edit_href = f'<a href="?student={student_id}&sbornik_id={self_number}&action=show_form_add_mest_sbornik">Редактировать сборник</a>'
        remove_href = f'<a href="?student={student_id}&sbornik_id={self_number}&action=remove_sbornik">Удалить сборник</a>'
        print(f'''<tr bgcolor=#bfffff>
            <td align=center>{self_number + 1}</td>
            <td align=center>{self.name}</td>
            <td align=center>{self.developer}</td>
            <td align=center>{self.date}</td>
            <td align=center>{self.organization}</td>
            <td align=center>{edit_href} {remove_href}</td>
            </tr>
            ''')
    
    def edit_self(self, q):
        self.name = q['name'].value
        self.developer = q['developer'].value
        self.date = q['date'].value
        self.organization = q['organization'].value
