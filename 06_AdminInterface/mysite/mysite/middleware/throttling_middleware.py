from django.http import HttpRequest, HttpResponse
import datetime


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class ThrottlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.__time_last_request = datetime.datetime.now()

    def __call__(self, request: HttpRequest):
        ip = get_client_ip(request)
        delta_time = (datetime.datetime.now() - self.__time_last_request).seconds
        self.__time_last_request = datetime.datetime.now()
        if delta_time < 1:
            return HttpResponse('У нас есть подозрение, что вы робот. Слишком частые запросы.')
        response: HttpResponse = self.get_response(request)
        return response
