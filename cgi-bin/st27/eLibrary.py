from .Sbornik import Sbornik
from .MestSbornik import MestSbornik
import pickle

class eLibrary:
    library=[]
    
    def __init__(self, q, selfurl):
        self.read_from_file()
        self.q = q
        self.selfurl = selfurl
        self.st_id = '{0}?student={1}'.format(selfurl, q['student'].value)

    def show_table(self):
        print('<br>','<br>','<table border="2" border cellspacing="0" cellpadding=5 align=left bgcolor = 99CCFF >')
        print('<tr><th>№</th><th>Наименование Сборника</th><th>Разработчик Сборника</th><th>Дата утверждения</th><th>Организация</th><th>Действие</th></tr>')
        for i, sbornik in enumerate(self.eLibrary):
            sbornik.show_sbornik(self.q, i)
        print('</table>', '<br>','<br>','<br>','<br>')

    def show_menu(self):
        print('Меню:')
        print('<br>','<a href={0}?student={1}&action={2}&sb_fl={3}&sbornik_id={4}>1. Добавить Сборник</a>'
            .format(self.selfurl, self.q.getvalue('student'), 'show_form_add_sbornik', '1', '-1'))
        print('<br>','<a href={0}?student={1}&action={2}&sb_fl={3}&sbornik_id={4}>2. Добавить местный Сборник</a>'
            .format(self.selfurl, self.q.getvalue('student'), 'show_form_add_mest_sbornik', '0', '-1'))
        print('<br>','<a href={0}?student={1}&action={2}>3. Очистить</a>'
            .format(self.selfurl, self.q.getvalue('student'), 'clear'))
        print('<br>','<a href="{0}">Назад</a>'.format(self.selfurl))
        
    def show_actions_menu(self):
        if len(self.eLibrary) == 0:
            self.show_menu()
        else:
            self.show_menu()
            self.show_table()

    def save_sbornik(self):
        if int(self.q['sbornik_id'].value) == -1:
            if int(self.q['sb_fl'].value) == 1:
                sbornik = Sbornik(
                        self.q.getvalue('name'),
                        self.q.getvalue('developer'),
                        self.q.getvalue('date')
                    )
            else:
                sbornik = MestSbornik(
                        self.q.getvalue('name'),
                        self.q.getvalue('developer'),
                        self.q.getvalue('date'),
                        self.q.getvalue('organization'),
                    )
            self.eLibrary.append(sbornik)
        else:
            sbornik = self.eLibrary[int(self.q['sbornik_id'].value)]
            sbornik.edit_self(self.q)
        
        self.write_to_file()
        self.show_page()

    def show_form_add_sbornik(self):
        _id = int(self.q.getvalue('sbornik_id'))

        if (_id == -1):
            sbornik = Sbornik(None, None, None)
        else:
            self.read_from_file()
            sbornik = self.eLibrary[_id]
            
        print('''<form action={0}>
                     <input type=hidden name=student value={1}>
                     <input type=hidden name=action value={2}>
                     <input type=hidden name=sbornik_id value={3}>
                     <input type=hidden name=sb_fl value={4}>
                     <table>                
                         <tr>
                             <td>Наименование Сборника:</td>
                             <td><input value ={5} type=text name=name></td>
                         </tr>
                         <tr>
                             <td>Разаботчик Сборника:</td>
                             <td><input value ={6} type=text name=developer><br></td>
                         </tr>
                         <tr>
                             <td>Дата утверждения:</td>
                             <td><input value ={7} type=text name=date></td>
                         </tr>                
                     </table> 
                     <input type=submit value="Записать Сборник">               
                 </form>'''.format(self.selfurl,self.q.getvalue('student'),'save_sbornik', self.q.getvalue('sbornik_id'), self.q.getvalue('sb_fl'), sbornik.name, sbornik.developer, sbornik.date))
    
    def show_form_add_mest_sbornik(self):
        _id = int(self.q.getvalue('sbornik_id'))

        if (_id == -1):
            sbornik = MestSbornik(None, None, None, None)
        else:
            self.read_from_file()
            sbornik = self.eLibrary[_id]
            
        print('''<form>
                     <input type=hidden name=student value={1}>
                     <input type=hidden name=action value={2}>
                     <input type=hidden name=sbornik_id value={3}>
                     <input type=hidden name=sb_fl value={4}>
                     <table>                
                         <tr>
                             <td>Наименование Сборника:</td>
                             <td><input value={5} type=text name=name></td>
                         </tr>
                         <tr>
                             <td>Разаботчик Сборника:</td>
                             <td><input value={6} type=text name=developer><br></td>
                         </tr>
                         <tr>
                             <td>Дата утверждения:</td>
                             <td><input value={7} type=text name=date></td>
                         </tr>
                         <tr>
                             <td>Организация:</td>
                             <td><input value={8} type=text name=organization></td>
                         </tr>  
                     </table> 
                     <input type=submit value="Записать Сборник">               
                 </form>'''.format(self.selfurl,self.q.getvalue('student'),'save_sbornik', self.q.getvalue('sbornik_id'), self.q.getvalue('sb_fl'), sbornik.name, sbornik.developer, sbornik.date, sbornik.organization))

    def remove_sbornik(self):
        _id = int(self.q['sbornik_id'].value)

        self.read_from_file()
        del self.eLibrary[_id]
        self.write_to_file()

        self.show_page()

    def write_to_file(self):
        f = open('cgi-bin/st27/eLibrary.dat', 'wb')
        pickle.dump(self.eLibrary, f)
        f.close()

    def read_from_file(self):
        f = open('cgi-bin/st27/eLibrary.dat', 'rb')
        self.eLibrary = pickle.load(f)
        f.close()

    def clear_library(self):
        self.read_from_file()
        self.eLibrary.clear()
        self.write_to_file()

        self.show_page()
        
    def show_page(self):
        print('<meta http-equiv=refresh content="0; URL=http://localhost{0}?student={1}">'
              .format(self.selfurl, self.q['student'].value))

