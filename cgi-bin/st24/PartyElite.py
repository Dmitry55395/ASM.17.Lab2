from .Comrade import Comrade


class PartyElite(Comrade):

    _position = None

    def __init__(self, list, q, selfurl):
        super().__init__(list, q, selfurl)

    def input(self):
        super().input()
        self._position = self._q['position'].value

    def edit(self, new_q):
        super().edit(new_q)
        self._position = new_q['position'].value

    def output(self):
        print("""
               <tr>
                   <td> {1} </td>
                   <td> {2} </td>
                   <td> {3} </td>
                   <td> {4} </td
                   <td>  </td>
                   <td><a href="?student={0}&id={1}&action=edit">Edit</a>
                   <br>
                   <a href="?student={0}&id={1}&action=remove_comrade">Delete</a
                   </td>
               </tr>
               """.format(self._q['student'].value, self.id, self._name, self._party_name, self._position))


