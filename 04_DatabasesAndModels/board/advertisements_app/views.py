from django.views import generic
from advertisements_app.models import Advertisements
import requests
import re


class AdvertisementListView(generic.ListView):
    model = Advertisements
    context_object_name = 'advertisement_list'
    queryset = Advertisements.objects.all()


class AdvertisementDetailView(generic.DetailView):
    model = Advertisements

    def get_context_data(self, **kwargs):
        count = self.object.number_views
        count += 1
        adv = Advertisements.objects.get(id=self.object.id)
        adv.number_views = count
        adv.save()
        context = super().get_context_data(**kwargs)
        # req_yandex = requests.get('https://yandex.ru/search/?clid=2574585&lr=20040&text=USD+MOEX&win=568&wiz=finance')
        # req_yandex.encoding = 'utf-8'
        # usd_rate = float(re.search(r'Доллар США = \d*,\d* Рос', req_yandex.text).group(0)[13:18].replace(',', '.'))
        # context['usd'] = round(self.object.price / usd_rate, 2)
        context['number_views'] = count
        return context


