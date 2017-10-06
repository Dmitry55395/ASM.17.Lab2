from .client import *
class Vipclient(Client):
    def __init__(self, q, selfurl):
        Client.__init__(self, q, selfurl)
        self.setParkingPlace(q.getfirst("parking_place", None))
        self.setPersonalTrener(q.getfirst("personal_trener", None))
    def edit(self,q):
        Client.edit(self,q)
        self.setParkingPlace(q.getfirst("parking_place", None))
        self.setPersonalTrener(q.getfirst("personal_trener", None))
    def setParkingPlace(self, inputValue):
        self.parking_place = inputValue
    def setPersonalTrener(self, inputValue):
        self.personal_trener = inputValue
    def getParkingPlace(self):
        return self.parking_place
    def getPersonalTrener(self):
        return self.personal_trener
    def __str__(self):
        return '<input type="text" class="form-control" value="' + str(self.getName()) + '"></td><td>Вип</td><td><input type="text" class="form-control" value="' + str(self.getAge()) + '"></td><td><input type="text" class="form-control" value="' + str(self.getWeight()) + '"></td><td> <input type="text" class="form-control" value="' + str(self.getPhone()) + '"></td>'+ '<td><input type="text" class="form-control" value="' + str(self.getParkingPlace()) + '"></td><td><input type="text" class="form-control" value="' + str(self.getPersonalTrener()) + '''"></td><td>
        <div class="container" style="width: 100%;">
            <div class="row">
                <a onclick="window.location.href=\''''+ '/cgi-bin/lab2.py' +'''?student=2&action=2&name='+this.parentNode.parentNode.parentNode.parentNode.firstChild.nextSibling.firstChild.value+'&age='+this.parentNode.parentNode.parentNode.parentNode.firstChild.nextSibling.nextSibling.nextSibling.firstChild.value+'&weight='+this.parentNode.parentNode.parentNode.parentNode.firstChild.nextSibling.nextSibling.nextSibling.nextSibling.firstChild.value+'&phone='+this.parentNode.parentNode.parentNode.parentNode.firstChild.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.firstChild.nextSibling.value+'&parking_place='+this.parentNode.parentNode.parentNode.parentNode.firstChild.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.firstChild.value+'&personal_trener='+this.parentNode.parentNode.parentNode.parentNode.firstChild.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.firstChild.value+'&editnum='+this.parentNode.parentNode.parentNode.parentNode.firstChild.firstChild.data" class="btn btn-primary a-btn-slide-text">
                    <span class="glyphicon glyphicon-edit" aria-hidden="true"></span>
                    <span><strong> edit</strong></span>
                </a>
                <a onclick="window.location.href=\''''+ '/cgi-bin/lab2.py' +'''?student=2&action=3&delnum='+this.parentNode.parentNode.parentNode.parentNode.firstChild.firstChild.data" class="btn btn-primary a-btn-slide-text">
                    <span class="glyphicon glyphicon-remove" aria-hidden="true"></span>
                    <span><strong> del</strong></span>
                </a>
            </div>
        </div></td></tr>'''