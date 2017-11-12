class Comrade:
    _name = None
    _party_name = None
    id = None

    def __init__(self, list, q, selfurl):
        self.id = list.get_id()
        self._q = q
        self._selfurl = selfurl

    def input(self):
        self._name = self._q['fullname'].value
        self._party_name = self._q['party_name'].value

    def edit(self, new_q):
        self._name =  new_q['fullname'].value
        self._party_name = new_q['party_name'].value

    def output(self):
        print("""
                <tr>
                    <td> {1} </td>
                    <td> {2} </td>
                    <td> {3} </td>
                    <td>  </td
                    <td>  </td>
                    <td><a href="?student={0}&id={1}&action=edit">Edit</a>
                    <br>
                    <a href="?student={0}&id={1}&action=remove_comrade">Delete</a
                    </td>
                </tr>
                """.format(self._q['student'].value, self.id, self._name, self._party_name))
