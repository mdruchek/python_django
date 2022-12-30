import datetime
import os


class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        with open(os.path.join('..', 'user_info.log'), 'a', encoding='utf8') as file:
            file.write('date: {date} / method: {method}/ url: {scheme}://{host}{path}\n'.format(date=str(datetime.datetime.now()),
                                                                                                method=request.method,
                                                                                                scheme=request.scheme,
                                                                                                host=request.get_host(),
                                                                                                path=request.path))
        return response
