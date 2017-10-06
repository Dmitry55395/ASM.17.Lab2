class Client:
    def __init__(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        self.setName(q.getfirst("name", None))
        self.setGender(q.getfirst("gender", None))        
        self.setAge(q.getfirst("age", None))
        self.setWeight(q.getfirst("weight", None))
        self.setPhone(q.getfirst("phone", None))
    def edit(self,q):
        self.setName(q.getfirst("name", None))
        self.setGender(q.getfirst("gender", None))        
        self.setAge(q.getfirst("age", None))
        self.setWeight(q.getfirst("weight", None))
        self.setPhone(q.getfirst("phone", None))
    def setName(self, inputValue):
        self.name = inputValue
    def setGender(self, inputValue):
        self.gender = inputValue
    def setAge(self, inputValue):
        self.age = inputValue
    def setWeight(self, inputValue):
        self.weight = inputValue
    def setPhone(self, inputValue):
        self.phone = inputValue
    def getName(self):
        return self.name
    def getGender(self):
        return self.gender
    def getAge(self):
        return self.age
    def getWeight(self):
        return self.weight
    def getPhone(self):
        return self.phone
    def __str__(self):
        self.string = '<input type="text" class="form-control" value="' + str(self.getName()) + '"></td><td>Обычный</td><td><input type="text" class="form-control" value="' + str(self.getAge()) + '"></td><td><input type="text" class="form-control" value="' + str(self.getWeight()) + '"></td><td> <input type="text" class="form-control" value="' + str(self.getPhone()) + '''"></td><td>-</td><td>-</td><td>
        <div class="container" style="width: 100%;">
            <div class="row">
                <a onclick="window.location.href=\''''+ '/cgi-bin/lab2.py' +'''?student=2&action=2&name='+this.parentNode.parentNode.parentNode.parentNode.firstChild.nextSibling.firstChild.value+'&age='+this.parentNode.parentNode.parentNode.parentNode.firstChild.nextSibling.nextSibling.nextSibling.firstChild.value+'&weight='+this.parentNode.parentNode.parentNode.parentNode.firstChild.nextSibling.nextSibling.nextSibling.nextSibling.firstChild.value+'&phone='+this.parentNode.parentNode.parentNode.parentNode.firstChild.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.firstChild.nextSibling.value+'&editnum='+this.parentNode.parentNode.parentNode.parentNode.firstChild.firstChild.data" class="btn btn-primary a-btn-slide-text">
                    <span class="glyphicon glyphicon-edit" aria-hidden="true"></span>
                    <span><strong> edit</strong></span>
                </a>
                <a onclick="window.location.href=\''''+ '/cgi-bin/lab2.py' +'''?student=2&action=3&delnum='+this.parentNode.parentNode.parentNode.parentNode.firstChild.firstChild.data" class="btn btn-primary a-btn-slide-text">
                    <span class="glyphicon glyphicon-remove" aria-hidden="true"></span>
                    <span><strong> del</strong></span>
                </a>
            </div>
        </div></td></tr>'''
        return self.string