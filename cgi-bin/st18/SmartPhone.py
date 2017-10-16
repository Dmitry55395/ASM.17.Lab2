from .MobilePhone import MobilePhone


class SmartPhone(MobilePhone):
    def __init__(self, brand, screen_size, housing_type, os, ram):
        super().__init__(brand, screen_size, housing_type)
        self.os = os
        self.ram = ram

    @staticmethod
    def get_color():
        return '#80ffaa'

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
                    <tr>
                        <td>OS:</td>
                        <td><input type=text name=os></td>
                    </tr>
                    <tr>
                        <td>RAM:</td>
                        <td><input type=text name=ram></td>
                    </tr>                
                </table> 
                <input type=submit>               
            </form>
        '''.format(
            self_url,
            q.getvalue('student'),
            'insert_smart_phone',
            SmartPhone.get_color()
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
                    <tr>
                        <td>OS:</td>
                        <td><input type=text name=os value={8}></td>
                    </tr>
                    <tr>
                        <td>RAM:</td>
                        <td><input type=text name=ram value={9}></td>
                    </tr>                
                </table> 
                <input type=submit>               
            </form>
        '''.format(
            self_url,
            q.getvalue('student'),
            'edit_phone',
            q.getvalue('id'),
            SmartPhone.get_color(),
            self.brand,
            self.screen_size,
            self.housing_type,
            self.os,
            self.ram
        ))

    def edit(self, q):
        super().edit(q)
        self.os = q.getvalue('os')
        self.ram = q.getvalue('ram')
