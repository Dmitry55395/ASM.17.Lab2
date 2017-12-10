class Native:
    def __init__(self, name, album_name, year):
        self.name = name
        self.album_name = album_name
        self.year = year

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
                </table> 
                <input type=submit>               
            </form>
        '''.format(
            self_url,
            q.getvalue('student'),
            'insert_native',
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
            self.year
        ))

    def edit(self, q):
        self.name = q.getvalue('name')
        self.album_name = q.getvalue('album_name')
        self.year = q.getvalue('year')
