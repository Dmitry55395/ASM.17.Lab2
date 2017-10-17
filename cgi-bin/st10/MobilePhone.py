class MobilePhone:
    def __init__(self, brand, screen_size, housing_type):
        self.brand = brand
        self.screen_size = screen_size
        self.housing_type = housing_type

    @staticmethod
    def get_color():
        return '#ccffcc'

    @staticmethod
    def show_add_form(q, self_url):
        print('''
            <form action={0}>
                <input type=hidden name=student value={1}>
                <input type=hidden name=action value={2}>
                <table bgcolor={3}>                
                    <tr>
                        <td>Brand:</td>
                        <td><input type=text name=brand></td>
                    </tr>
                    <tr>
                        <td>Screen size:</td>
                        <td><input type=text name=screen_size><br></td>
                    </tr>
                    <tr>
                        <td>Housing type:</td>
                        <td><input type=text name=housing_type></td>
                    </tr>                
                </table> 
                <input type=submit>               
            </form>
        '''.format(
            self_url,
            q.getvalue('student'),
            'insert_mobile_phone',
            MobilePhone.get_color()
        ))

    def show_edit_form(self, q, self_url):
        print('''
            <form action={0}>
                <input type=hidden name=student value={1}>
                <input type=hidden name=action value={2}>
                <input type=hidden name=id value={3}>                
                <table bgcolor={4}>                
                    <tr>
                        <td>Brand:</td>
                        <td><input type=text name=brand value={5}></td>
                    </tr>
                    <tr>
                        <td>Screen size:</td>
                        <td><input type=text name=screen_size value={6}><br></td>
                    </tr>
                    <tr>
                        <td>Housing type:</td>
                        <td><input type=text name=housing_type value={7}></td>
                    </tr>                
                </table>
                <input type=submit>               
            </form>
        '''.format(
            self_url,
            q.getvalue('student'),
            'edit_phone',
            q.getvalue('id'),
            self.get_color(),
            self.brand,
            self.screen_size,
            self.housing_type
        ))

    def edit(self, q):
        self.brand = q.getvalue('brand')
        self.screen_size = q.getvalue('screen_size')
        self.housing_type = q.getvalue('housing_type')
