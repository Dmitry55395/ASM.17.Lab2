from .Comrade import Comrade
from .PartyElite import PartyElite
import pickle


class CommunistParty:
    __path = "cgi-bin/st24/uploading_data.pkl"
    __party_list = []
    __id = 0

    def __init__(self, q, selfurl):
        self.__q = q
        self.__selfurl = selfurl
        return

    def get_id(self):
        self.__id += 1
        return self.__id

    def print_style_of_form(selfe):
        print("""<style> 
                   input[type=text] {
                    width: 130px;
                    box-sizing: border-box;
                    border: 2px solid #ccc;
                    border-radius: 4px;
                    font-size: 16px;
                    background-color: white;
                    background-position: 10px 10px; 
                    background-repeat: no-repeat;
                    padding: 12px 20px 12px 10px;
                    -webkit-transition: width 0.4s ease-in-out;
                    transition: width 0.4s ease-in-out;
                }
                input[type=text]:focus {
                    width: 100%;
                }
                input[type=button], input[type=submit], input[type=reset] {
                    background-color: red;
                    border: none;
                    color: white;
                    padding: 16px 32px;
                    text-decoration: none;
                    margin: 4px 2px;
                    cursor: pointer;
                }
                </style> """)

    def show_comrade_form(self, comrade=None):
        self.print_style_of_form()
        if (comrade == None):
            print("""
                <div align='center'>
                        <form action="{0}" align='center'>
                           <input type="hidden" name = "action" value="add_comrade">
                           <input type="hidden" name = "student" value={1}>
                           <input type="hidden" name = "id" value='0'>
                               Fullname: <input type="text" value='' name="fullname"><br>
                               Party name: <input type="text" value='' name="party_name"><br>
                           <input type="submit" value="Save"><br>
                           <a href="{0}?student={1}">Back</a><br>
                        </form>
                </div>
                   """.format(self.__selfurl, self.__q['student'].value))
        else:
            print("""
                <div align='center'>
                      <form action="{0}">
                         <input type="hidden" name = "action" value="edit_in_party">
                         <input type="hidden" name = "student" value={1}>
                         <input type="hidden" name = "id" value='{2}'>
                             Fullname: <input type="text" value='{3}' name="fullname"><br>
                             Party name: <input type="text" value='{4}' name="party_name"><br>
                         <input type="submit" value="Save"><br>
                         <a href="{0}?student={1}">Back</a><br>
                      </form>
                </div>
                 """.format(self.__selfurl, self.__q['student'].value, comrade.id, comrade._name, comrade._party_name))

    def show_party_elite_form(self, party_elite=None):
        self.print_style_of_form()
        if (party_elite == None):
            print("""
                        <div align='center'>
                           <form action="{0}" >
                              <input type="hidden" name = "action" value="add_party_elite">
                              <input type="hidden" name = "student" value={1}>
                              <input type="hidden" name = "id" value='0'>
                                  Fullname: <input type="text" value='' name="fullname"><br>
                                  Party name: <input type="text" value='' name="party_name"><br>
                                  Position: <input type="text" value='' name="position"><br>
                              <input type="submit" value="Save"><br>
                              <a href="{0}?student={1}">Back</a><br>
                           </form>
                        </div>
                      """.format(self.__selfurl, self.__q['student'].value))
        else:
            print("""
                    <div align='center'>
                      <form action="{0}" align='center'>
                         <input type="hidden" name = "action" value="edit_in_party">
                         <input type="hidden" name = "student" value={1}>
                         <input type="hidden" name = "id" value='{2}'>
                             Fullname: <input type="text" value='{3}' name="fullname"><br>
                             Party name: <input type="text" value='{4}' name="party_name"><br>
                             Position: <input type="text" value='{5}' name="position"><br>
                         <input type="submit" value="Save"><br>
                         <a href="{0}?student={1}">Back</a><br>
                      </form>
                    </div>
                 """.format(self.__selfurl, self.__q['student'].value, party_elite.id, party_elite._name,
                            party_elite._party_name, party_elite._position))

    def add_comrade(self):
        comrade = Comrade(self, self.__q, self.__selfurl)
        comrade.input()
        self.__party_list.append(comrade)
        self.write_to_file()
        self.print_party_list()

    def add_party_elite(self):
        party_elite = PartyElite(self, self.__q, self.__selfurl)
        party_elite.input()
        self.__party_list.append(party_elite)
        self.write_to_file()
        self.print_party_list()

    def edit_in_party(self):
        id = self.__q['id'].value
        try:
            next(x for x in self.__party_list if int(id) == x.id).edit(self.__q)
            self.write_to_file()
            self.print_party_list()
        except Exception:
            return

    def print_party_list(self):
        print("""<style> 
                    table {
                        border-spacing: 0 10px;
                        font-family: 'Open Sans', sans-serif;
                        font-weight: bold;
                    }
                    th {
                        padding: 10px 20px;
                        background: #56433D;
                        color: #F9C941;
                        border-right: 2px solid; 
                        font-size: 0.9em;
                    }
                    th:first-child {
                        text-align: left;
                    }
                    th:last-child {
                        border-right: none;
                    }
                    td {
                        vertical-align: middle;
                        padding: 10px;
                        font-size: 14px;
                        text-align: center;
                        border-top: 2px solid #56433D;
                        border-bottom: 2px solid #56433D;
                        border-right: 2px solid #56433D;
                    }
                    td:first-child {
                        border-left: 2px solid #56433D;
                        border-right: none;
                    }
                    td:nth-child(2){
                        text-align: left;
                    }
            </style> """)

        print("""
            <table border = '3' align='center'>
                <caption>Time for <font color = 'red'> COMMUNISM <font></caption>
                <tr>
                    <td>
                        ID
                    </td>
                    <td>
                        Fullname
                    </td>
                    <td>
                        Party Name
                    </td>
                    <td>
                        Position
                    </td>
                    <td>
                        Actions
                    </td>
                </tr>
              """)

        for person in self.__party_list:
            person.output()

        print("""</table><br>
                    <div  align='center'>
                        <a href="?student={0}&action=show_comrade_form">Add comrade</a><br>
                        <a href="?student={0}&action=show_party_elite_form">Add party elite</a><br>
                        <a href="?student={0}&action=clear_list">Clear party list</a><br>
                        <a href="{1}">Back</a><br>
                    </div>""".format(
            self.__q['student'].value,
            self.__selfurl))

    def write_to_file(self):
        with open(self.__path, "wb") as f:
            pickle.dump([self.__party_list, self.__id], f)

    def read_from_file(self):
        try:
            with open(self.__path, "rb") as f:
                [self.__party_list, self.__id] = pickle.load(f)
        except Exception:
            return

    def clear_party_list(self):
        self.__party_list.clear()
        self.write_to_file()
        self.print_party_list()

    def remove(self):
        id = self.__q['id'].value
        try:
            del self.__party_list[next(i for i, x in enumerate(self.__party_list) if int(id) == x.id)]
            self.write_to_file()
            self.print_party_list()
        except StopIteration:
            return

    def edit(self):
        id = self.__q['id'].value
        try:
            item = next(x for x in self.__party_list if int(id) == x.id)
            if (type(item) is Comrade):
                self.show_comrade_form(item)
            else:
                self.show_party_elite_form(item)
        except StopIteration:
            return
