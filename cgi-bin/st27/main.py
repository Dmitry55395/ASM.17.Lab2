from .http.Router import Router


def main(params, url):
    router = Router(url, params)
    router.start()
