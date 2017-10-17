from .Model import *


class SuperModel(Model):
    magazine = ' '

    def __init__(self):
        pass

    def edit_self(self, q):
        self.surname = q['surname'].value
        self.name = q['name'].value
        self.age = q['age'].value
        self.growth = q['growth'].value
        self.weight = q['weight'].value
        self.magazine = q['magazine'].value

    def show_self(self, q, self_number):
        student_id = q['student'].value
        edit_href = f'<a href="?student={student_id}&model_id={self_number}&is_supermodel=1&action=show_edit">Edit</a>'
        remove_href = f'<a href="?student={student_id}&model_id={self_number}&action=remove_model">Remove</a>'
        print(f'''<tr bgcolor=#e0ff82>
            <td align=center>{self_number + 1}</td>
            <td align=center>{self.surname}</td>
            <td align=center>{self.name}</td>
            <td align=center>{self.age}</td>
            <td align=center>{self.growth}</td>
            <td align=center>{self.weight}</td>
            <td align=center>{self.magazine}</td>
            <td align=center>{edit_href} {remove_href}</td>
            </tr>
            ''')

