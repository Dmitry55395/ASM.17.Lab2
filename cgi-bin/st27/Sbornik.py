class Sbornik:
    
    def __init__(self, name, developer, date):
        self.name = name
        self.developer = developer
        self.date = date

    def show_sbornik(self, q, self_number):
        student_id = q['student'].value
        edit_href = f'<a href="?student={student_id}&sbornik_id={self_number}&action=show_form_add_sbornik">Редактировать сборник</a>'
        remove_href = f'<a href="?student={student_id}&sbornik_id={self_number}&action=remove_sbornik">Удалить сборник</a>'
        print(f'''<tr bgcolor=#bfbfff>
            <td align=center>{self_number + 1}</td>
            <td align=center>{self.name}</td>
            <td align=center>{self.developer}</td>
            <td align=center>{self.date}</td>
            <td align=center  bgcolor=#bfbfbf></td>
            <td align=center>{edit_href} {remove_href}</td>
            </tr>
            ''')

    def edit_self(self, q):
        self.name = q['name'].value
        self.developer = q['developer'].value
        self.date = q['date'].value
