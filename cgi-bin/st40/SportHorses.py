from .Horses import Horses


class SportHorses(Horses):
    def __init__(self, name, age, color, type_of_sport):
        Horses.__init__(self, name, age, color)
        self.type_of_sport = type_of_sport
   
    
    def show_add_form(q, self_url):
        print('''
            <form action={0}>
                <input type=hidden name=student value={1}>
                <input type=hidden name=action value={2}>
                <table bgcolor={3}>                
                  <tr> <td>Введите имя лошади:</td>
                        <td><input type=text value="horse" name=name></td> </tr>
						
                    <tr> <td>Введите возраст лошади:</td>
                        <td><input type=text  value="15" name=age><br></td> </tr>
						
                    <tr> <td>Введите масть лошади:</td>
                        <td><input type=text value="black" name=color></td> </tr>  
						
                    <tr> <td>Введите вид спорта лошади:</td>
                        <td><input type=text value="jumping"  name=type_of_sport></td></tr>                
                </table> 
                <input type=submit>               
            </form>
        '''.format(self_url,q.getvalue('student'),'add_sport_horse', "#d7e7f7" ))

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
                    <tr>
                        <td>Введите вид спорта лошади:</td>
                        <td><input type=text name=type_of_sport value={8}></td>
                    </tr>                
                </table> 
                <input type=submit>               
            </form>
        '''.format(self_url, q.getvalue('student'),'edit_horse',q.getvalue('id'),
            "#d7e7f7", self.name, self.age, self.color, self.type_of_sport ))

    def edit(self, q):
        Horses.edit(self, q)
        self.type_of_sport = q.getvalue('type_of_sport')
