from .vipclient import *
import pickle
class Customers:
    def __init__(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        self.customer = []
    def add(self, x):
        self.customer.append(x)
    def edit(self, num, q):
        self.customer[num].edit(q)
    def delete(self,num):
        self.customer.pop(num)
    def clear(self):
        self.customer = []
    def save(self):
        pickle.dump( self.customer, open( "cgi-bin/st01/pickledata.p", "wb" ) )
    def load(self):
        self.customer = pickle.load( open( "cgi-bin/st01/pickledata.p", "rb" ) )
    def __len__(self):
        return len(self.customer)
    def __str__(self):
        string = '''<thead class="thead-inverse">
                        <tr class="active">
                            <th>№</th>
                            <th>Клиент</th>
                            <th>Тип</th>
                            <th>Возраст</th>
                            <th>Вес</th>
                            <th>Телефон</th>
                            <th>Парковочное<br>место</th>
                            <th>Имя персонального<br>тренера</th>
                            <th>Действие</th>
                        </tr>
                    </thead>'''
        count = 1
        if self.customer:
            for e in self.customer:
                string =string + '<tr><td>' +str(count) + '</td><td>' + str(e)
                count +=  1          
        else:
            string="Список пуст\n"
        add_tr = '''<tr>
            <td></td>
            <td><input type="text" class="form-control" id="name"></td>
            <td>
                <select class="form-control selectpicker" id="typeadd" style="width:110">
                    <option value=1>Обычный</option>
                    <option value=2>Вип</option>
                </select>

            </td>
            <td><input type="text" class="form-control" style="width:50" id="age"></td>
            <td><input type="text" class="form-control" style="width:50" id="weight"></td>
            <td><input type="text" class="form-control" id="phone"></td>
            <td><input type="text" class="form-control" style="width:80" id="parking_place"></td>
            <td><input type="text" class="form-control" id="personal_trener"></td>
            <td><div class="container" style="width: 140;">
                <div class="row">
                    <a id="addhref" onclick="window.location.href=\''''+ self.selfurl +'''?student=2&action=1&name='+$('#name')[0].value+'&age='+$('#age')[0].value+'&weight='+$('#weight')[0].value+'&phone='+$('#phone')[0].value+'&parking_place='+$('#parking_place')[0].value+'&personal_trener='+$('#personal_trener')[0].value+'&typeadd='+$('#typeadd')[0].value" class="btn btn-primary a-btn-slide-text">
                        <span class="glyphicon glyphicon-plus" aria-hidden="true"></span>
                        <span><strong> add</strong></span>
                    </a> 
                </div>
                </div>
            </td>
        </tr>'''
        return '<div style="margin-top: 20px" class="container"><table class="table table-hover table-bordered table-inverse">' + string + add_tr + '</table></div>'