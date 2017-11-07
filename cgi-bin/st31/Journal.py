import pickle, os

from .Run import Run
from .Marathon import Marathon
from .Form import Form

STORAGE_FILENAME = 'cgi-bin/st31/runJournal.dat'

class Journal:
    def __init__(self):
        self.runs = []
        
    def save(self):
        with open(STORAGE_FILENAME, 'wb') as f:
            pickle.dump(self.runs, f)
        
    def load(self):
        if os.path.getsize(STORAGE_FILENAME) > 0:
            with open(STORAGE_FILENAME, 'rb') as f:
                unpickler = pickle.Unpickler(f)
                self.runs = unpickler.load()
        
    def add(self, q):
        if 'type' in q:
            entry = Run()
            if q['type'].value == 'marathon':
                entry = Marathon()
            form = Form(q, entry)
            if form.isOk():
                print("Запись сохранена.")
                entry.update(q)
                self.runs.append(entry)
                self.save()
            form.show()
        else:
            print("Нужно указать тип записи.")
        
    def delete(self, q):
        if 'id' in q:
            runId = int(q["id"].value)
            if -1 < runId < len(self.runs):
                self.runs.pop(runId)
                self.save()
                print("Запись удалена.")
            else:
                print("Нет записи с таким номером.")
        else:
            print("Нужно указать номер записи.")
        
    def edit(self, q):
        if 'id' in q:
            runId = int(q["id"].value)
            if -1 < runId < len(self.runs):
                entry = self.runs[runId]
                form = Form(q, entry)
                if form.isOk():
                    print("Запись отредактирована")
                    entry.update(q)
                    self.save()
                form.show()
            else:
                print("Нет записи с таким номером.")
        else:
            print("Нужно указать номер записи.")
            
    def clear(self, q):
        self.runs.clear()
        self.save()
        print("Журнал очищен.")