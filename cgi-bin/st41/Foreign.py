from .Native import Native


class Foreign(Native):
    def __init__(self, name, album_name, year, country):
        super().__init__(name, album_name, year)
        self.country = country

    @staticmethod
    def show_add_form(q, self_url):
        print('''
            <form action={0} align=center>
                <input type=hidden name=student value={1}>
                <input type=hidden name=action value={2}>
                <table align=center>                
                    <tr>
                        <td>Name:</td>
                        <td><input type=text name=name></td>
                    </tr>
                    <tr>
                        <td>Album name:</td>
                        <td><input type=text name=album_name><br></td>
                    </tr>
                    <tr>
                        <td>Year:</td>
                        <td><input type=text name=year></td>
                    </tr>
                    <tr>
                        <td>Country:</td>
                        <td><input type=text name=country></td>
                    </tr>      
                </table> 
                <input type=submit>               
            </form>
        '''.format(
            self_url,
            q.getvalue('student'),
            'insert_foreign',
        ))

    def show_edit_form(self, q, self_url):
        print('''
            <form action={0} align=center>
                <input type=hidden name=student value={1}>
                <input type=hidden name=action value={2}>
                <input type=hidden name=id value={3}>
                <table align=center>                
                    <tr>
                        <td>Name:</td>
                        <td><input type=text name=name value={4}></td>
                    </tr>
                    <tr>
                        <td>Album name:</td>
                        <td><input type=text name=album_name value={5}><br></td>
                    </tr>
                    <tr>
                        <td>Year:</td>
                        <td><input type=text name=year value={6}></td>
                    </tr>
                    <tr>
                        <td>Country:</td>
                        <td><input type=text name=country value={7}></td>
                    </tr>
                </table> 
                <input type=submit>               
            </form>
        '''.format(
            self_url,
            q.getvalue('student'),
            'edit',
            q.getvalue('id'),
            self.name,
            self.album_name,
            self.year,
            self.country,
        ))

    def edit(self, q):
        super().edit(q)
        self.country = q.getvalue('country')
