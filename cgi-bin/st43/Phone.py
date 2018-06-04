class Phone:

    def __init__(self):
        self.vendor = None
        self.model = None

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
        print('<hr/>')
        print('<p><strong><input type="submit" value="Add" /></strong></p>')
        print('<input type="hidden" name = "act" value = "ph" >')
        print('</form></td></tr></table>')

    def set_data(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        if ('vendor' in self.q):
            self.vendor = self.q['vendor'].value
        if ('model' in self.q):
            self.model = self.q['model'].value

    def get_vendor(self):
        return self.vendor

    def get_model(self):
        return self.model
