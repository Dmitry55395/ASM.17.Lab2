from .category import *
import cgi

class Dish(Category):
    def __init__(self, q, selfurl):
        super().__init__(q, selfurl)
        self.name=""
        self.price=""
        self.weight=""
        self.q=q
        self.selfurl=selfurl
    
    def read(self):
        Category.read(self)
        if ('name' in self.q):
            self.name = self.q['name'].value
        else: self.name = ""
        if ('price' in self.q):
             self.price = self.q['price'].value
        else: self.display = ""
        if ('weight' in self.q):
             self.weight = self.q['weight'].value
        else: self.weight = ""

    def write(self):
        Category.write(self)
        print('<td>{0}</td>'.format(self.name))
        print('<td>{0}</td>'.format(self.price))
        print('<td>{0}</td>'.format(self.weight))

    def write_ch(self):
        Category.write_ch(self)
        print('<br>Название блюда:<br><input type="display" name="name" value="{0}">'.format(self.name))
        print('<br>Цена:<br><input type="display" name="price" value="{0}">'.format(self.price))
        print('<br>Вес (гр):<br><input type="display" name="weight" value="{0}">'.format(self.weight))
    	

    
    
