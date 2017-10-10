class Form:
    def __init__(self, q, model):
        self.q = q
        self.model = model
        
    def getValue(self, attr):
        if attr in self.q:
            return self.q[attr].value
        return getattr(self.model, attr)
    
    def show(self):
        print('<form>')
        print('<input type=hidden value={0} name="student">'.format(self.q['student'].value))
        print('<input type=hidden value={0} name="act">'.format(self.q['act'].value))
        if 'type' in self.q:
            print('<input type=hidden value={0} name="type">'.format(self.q['type'].value))
        if 'id' in self.q:
            print('<input type=hidden value={0} name="id">'.format(self.q['id'].value))

        for i, attr in enumerate(self.model.attrs):
            print('{0}: <input type="text" size=5 name="{1}" value={2}>'.format(self.model.names[i], attr, self.getValue(attr)))
        print('<input type=submit value="Сохранить">')
        print('</form>')
        
    def isOk(self):
        try:
            return int(self.q["length"].value) > 0 and int(self.q["time"].value) > 0
        except:
            return False