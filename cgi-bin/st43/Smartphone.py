from .Phone import *


class Smartphone(Phone):

    def __init__(self):
        super().__init__()
        self.battery = None
        self.camera_res = None


    def rec(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        print('<table><tr><td>')
        print('<form action="{0}" method="get">'.format(self.selfurl))
        print('<input type="hidden" name = "index" value = "{0}" >'.format(self.q['index'].value))
        print('<input type="hidden" name = "student" value = "{0}" >'.format(self.q['student'].value))
        print('<h2><strong>Add new phone:</strong></h2>')
        print('<hr/>')
        print('<p><strong>Vendor <input required name = "vendor" type="text" value={0} /></strong></p>'.format(self.vendor))
        print('<p><strong>Model <input required name = "model" type="text" value={0} /></strong></p>'.format(self.model))
        print('<p><strong>Battery <input required name = "battery" type="text" value={0} /></strong></p>'.format(self.battery))
        print('<p><strong>Camera <input required name = "camera" type="text" value={0} /></strong></p>'.format(self.camera_res))
        print('<hr/>')
        print('<p><strong><input type="submit" value="Add" /></strong></p>')
        print('<input type="hidden" name = "act" value = "sph" >')
        print('</form></td></tr></table>')


    def set_data(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        super().set_data(q, selfurl)
        if 'battery' in self.q:
            self.battery = self.q['battery'].value
        if 'camera' in self.q:
            self.camera_res = self.q['camera'].value

    def get_battery(self):
        return self.battery

    def get_camera(self):
        return self.camera_res
