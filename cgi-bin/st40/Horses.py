class Horses:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    
    def show_add_form(q, self_url):
        print(''' <form action={0}>
                <input type=hidden name=student value={1}>
                <input type=hidden name=action value={2}>
                <table bgcolor={3}>                
                    <tr> <td>Введите имя лошади:</td>
                        <td><input type=text  value="horse" name=name></td> </tr>
						
                    <tr> <td>Введите возраст лошади:</td>
                        <td><input type=text value="10" name=age><br></td> </tr>
						
                    <tr> <td>Введите масть лошади:</td>
                        <td><input type=text value="color" name=color></td> </tr>  				
                </table> 
                <input type=submit>               
            </form>
        '''.format(self_url,  q.getvalue('student'),
            'add_horse', "#d7e7f7"   ))

    def show_form_for_edit(self, q, self_url):
        print('''
            <form action={0}>
                <input type=hidden name=student value={1}>
                <input type=hidden name=action value={2}>
                <input type=hidden name=id value={3}>                
                <table bgcolor={4}>                
                    <tr>
                        <td>Введите имя лошади:</td>
                        <td><input type=text name=name value={5}></td>
                    </tr>
                    <tr>
                        <<td>Введите возраст лошади:</td>
                        <td><input type=text name=age value={6}><br></td>
                    </tr>
                    <tr>
                        <<td>Введите масть лошади:</td>
                        <td><input type=text name=color value={7}></td>
                    </tr>    
                </table>
                <input type=submit>               
            </form>
        '''.format(self_url, q.getvalue('student'), 'edit_horse',q.getvalue('id'), 
		"#d7e7f7", self.name, self.age, self.color))

    def edit(self, q):
        self.name = q.getvalue('name')
        self.age = q.getvalue('age')
        self.color = q.getvalue('color')
		#self.breed = q.getvalue('breed')

		
		