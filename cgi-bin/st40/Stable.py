import os, cgi, pickle, cgitb, sys, codecs

from .Horses import Horses
from .SportHorses import SportHorses
import pickle

def loadTpl(file_name):
        with open(os.environ['PATH_TRANSLATED']+'/cgi-bin/st40/template/'+file_name+'.tpl', 'rt') as f:
                return f.read()

class Stable:
 new_Stable = []
 bd = 'cgi-bin/st40/all_horses.dat'

 def __init__(self):
  self.load_file()

 def main_menu(self, q, self_url):
  print('<meta http-equiv=refresh content="0; URL=' + self_url + '?student=' + q.getvalue('student') + '">')

 def show_horse(self, q, self_url):
  Horses.show_add_form(q, self_url)

 def show_sport_horse(self, q, self_url):
  SportHorses.show_add_form(q, self_url)	

 def show_list(self, q, self_url):
  print(loadTpl('Header'))
  print ('<br>')		
  print("<a href={0}>Назад в меню</a>".format(self_url))
  print ('<br>')
  print("<a href={0}?student={1}&action={2}>Добавить лошадь</a>"
              .format(self_url, q.getvalue('student'), 'show_horse'))
  print ('<br>')			  
  print("<a href={0}?student={1}&action={2}>Добавить спортивную лошадь</a>"
              .format(self_url, q.getvalue('student'), 'show_sport_horse'))
  print ('<br>')			  
  print("<a href={0}?student={1}&action={2}>Очистить лист</a>"
              .format(self_url, q.getvalue('student'), 'clear'))
  print ('<br>')
  print(loadTpl('Header_Table'))  
  print('<table border=1 cellspacing=0 cellpadding=7>')
  print('''
            <tr bgcolor=#adcef0>
                <th width=20px>№</th>
                <th width=100px>Name</th>
                <th width=50px>Age</th>
                <th width=100px>Color</th>
                <th width=100px>Type of sport</th>
                <th width=100px></th>
            </tr>
        ''')
  id = 0
  for horse in self.new_Stable:
    id += 1
    print('''
     <tr bgcolor=#d7e7f7>
                    <td align=center>{1}</td>                                
                    <td align=center>{2}</td>
                    <td align=center>{3}</td>
                    <td align=center>{4}</td>
                    <td align=center>{5}</td>
            '''.format('#d7e7f7',id,
                getattr(horse, 'name', '') or '',
                getattr(horse, 'age', '') or '',
                getattr(horse, 'color', '') or '',
                #getattr(horse, 'breed', '') or '',
                getattr(horse, 'type_of_sport', '') or ''
            ))
    print('''
       <td>
        <a href={0}?student={1}&id={2}&action={3}>Редактировать</a>
		<br>
        <a href={0}?student={1}&id={2}&action={4}>Удалить</a>
        </td> '''
	 .format(self_url,q.getvalue('student'),id,'show_edit_form','delete'))
    print('</tr>')
  print('</table>')

 def show_edit_form(self, q, self_url):
  id = int(q.getvalue('id'))
  _horse = self.new_Stable[id - 1]
  _horse.show_form_for_edit(q, self_url)

 def add_horse(self, q, self_url):
  new_horse = Horses(
    q.getvalue('name'),
    q.getvalue('age'),
    q.getvalue('color')
    #q.getvalue('breed')
   )
  self.new_Stable.append(new_horse)
  self.save_file()
  self.main_menu(q, self_url)

 def add_sport_horse(self, q, self_url):
  new_s_horse = SportHorses(
   q.getvalue('name'),
   q.getvalue('age'),
   q.getvalue('color'),
   #q.getvalue('breed'),
   q.getvalue('type_of_sport')
  )
  self.new_Stable.append(new_s_horse)
  self.save_file()
  self.main_menu(q, self_url)

 def delete(self, q, self_url):
  id = int(q.getvalue('id'))
  self.new_Stable.pop(id - 1)
  self.save_file()
  self.main_menu(q, self_url)

 def edit_horse(self, q, self_url):
  id = int(q.getvalue('id'))
  horse = self.new_Stable[id - 1]
  horse.edit(q)
  self.save_file()
  self.main_menu(q, self_url)
	
 def load_file(self):
  file = open(self.bd, 'rb')
  self.new_Stable = pickle.load(file)
  file.close()

 def save_file(self):
  file = open(self.bd, 'wb')
  pickle.dump(self.new_Stable, file)
  file.close()
  
 def clear(self, q, self_url):
  self.new_Stable.clear()
  self.save_file()
  self.main_menu(q, self_url)
		
	
	

