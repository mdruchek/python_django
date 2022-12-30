from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


def advertisement_list(request, *args, **kwargs):
    advertisements = [
        'Мастер на час',
        'Выведение из запоя',
        'Услуги экскаватора-погрузчика, гидромолота, ямобура'
    ]
    advertisements_1 = [
        'Мастер на час',
        'Выведение из запоя',
        'Услуги экскаватора-погрузчика, гидромолота, ямобура'
    ]
    return render(request, 'advertisements/advertisement_list.html', {'advertisements': advertisements,
                                                                      'advertisements_1': advertisements_1})


class Advertisements(View):
    advertisements = [
        'Мастер на час',
        'Выведение из запоя',
        'Услуги экскаватора-погрузчика, гидромолота, ямобура'
    ]

    message = ['Запрос на создание новой записи успешно выполнен']

    count_GET = 0
    count_POST = 0

    def get(self, request):
        Advertisements.count_GET += 1
        return render(request, 'advertisements/advertisements.html', {'advertisements': Advertisements.advertisements,
                                                                      'count_GET': Advertisements.count_GET,
                                                                      'count_POST': Advertisements.count_POST})

    def post(self, request):
        Advertisements.count_POST += 1
        return render(request, 'advertisements/advertisements.html', {'advertisements': Advertisements.message,
                                                                      'count_GET': Advertisements.count_GET,
                                                                      'count_POST': Advertisements.count_POST})


class Contacts(TemplateView):
    template_name = 'advertisements/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        context['address'] = 'г.Москва'
        context['telephone'] = '+7 (999) 123-45-67'
        context['email'] = 'exemple@mail.ru'
        return context

