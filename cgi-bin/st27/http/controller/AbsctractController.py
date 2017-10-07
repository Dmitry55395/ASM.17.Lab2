from abc import ABCMeta


class AbstractController(metaclass=ABCMeta):
    def __init__(self, request_url, request_params):
        self._request_url = request_url
        self._request_params = request_params

    @staticmethod
    def _render(view_class_ref, params):
        view = view_class_ref(params)
        view.render()

    @staticmethod
    def _redirect(url):
        print('<meta http-equiv=refresh content="0; URL=http://localhost' + url + '">')
