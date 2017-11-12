class Model:
    surname = 'None'
    name = 'None'
    age = 0
    growth = 0
    weight = 0

    def __init__(self):
        pass

    def edit_self(self, q):
        self.surname = q['surname'].value
        self.name = q['name'].value
        self.age = q['age'].value
        self.growth = q['growth'].value
        self.weight = q['weight'].value

    def show_self(self, q, self_number):
        student_id = q['student'].value
        edit_href = f'<a href="?student={student_id}&model_id={self_number}&is_supermodel=0&action=show_edit">Edit</a>'
        remove_href = f'<a href="?student={student_id}&model_id={self_number}&action=remove_model">Remove</a>'
        print(f'''<tr>
            <td align=center>{self_number + 1}</td>
            <td align=center>{self.surname}</td>
            <td align=center>{self.name}</td>
            <td align=center>{self.age}</td>
            <td align=center>{self.growth}</td>
            <td align=center>{self.weight}</td>
            <td align=center  bgcolor=#bfbfbf></td>
            <td align=center>{edit_href} {remove_href}</td>
            </tr>
            ''')