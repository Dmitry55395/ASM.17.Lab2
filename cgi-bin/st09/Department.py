from .Market import *
from .LoadTpl import *


class Department(Market):
    _department_name : str = ''
    _product_type : str = ''

    def __init__(self, q, instance_url):
        super().__init__(q, instance_url)

    def show(self, self_id):
        print(loadTpl('show_Department').format(
            self._q['student'].value,
            self_id,
            self._nickname,
            self._owner_name,
            self._address,
            self._department_name,
            self._product_type
        ))

    def show_edit(self):
        print(loadTpl('save_Department').format(
            self._instance_url,
            self._q['student'].value,
            self._q['market_id'].value,
            False,
            self._nickname,
            self._owner_name,
            self._address,
            self._department_name,
            self._product_type
        ))

    def set_parameters(self):
        super().set_parameters()
        self._department_name = self._q['department_name'].value
        self._product_type = self._q['product_type'].value
        
        
