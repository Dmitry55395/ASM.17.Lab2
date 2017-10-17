from .controller.CarController import CarController


class Router:
    def __init__(self, url, params):
        self.__url = url
        self.__params = params
        self.__car_controller = CarController(url, params)

    def __route_map(self):
        return {
            'car/show_list': self.__car_controller.index,
            'car/edit': self.__car_controller.edit,
            'car/update': self.__car_controller.update,
            'car/create': self.__car_controller.create,
            'car/store': self.__car_controller.store,
            'car/delete': self.__car_controller.destroy
        }

    def start(self):
        print("Content-type: text/html; charset=utf-8\n\n")
        try:
            route = self.__params.getvalue('route', 'car/show_list')
            handler_ref = self.__route_map().get(route)

            if handler_ref is None:
                raise RuntimeError('Unknown route')

            handler_ref()
        except Exception as e:
            print('Exception was thrown: ', e)
