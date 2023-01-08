from django.shortcuts import render
from django.views.generic.list import ListView
from  django.views.generic.detail import DetailView
from django.views import View
from app_news.models import News, Comment
from app_news.forms import NewsForm, CommentForm
from django.http.response import HttpResponseRedirect


class NewsListView(ListView):
    model = News
    paginate_by = 10
    ordering = ['-date_creation']
    queryset = News.objects.filter(activity=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inactive_news'] = News.objects.filter(activity=False).order_by('-date_creation')
        return context


class NewsDetailView(DetailView):
    model = News
    news_id = 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = kwargs['object'].comment_set.all()
        return context

    def post(self, request, **kwargs):
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment_form.cleaned_data['news'] = News.objects.get(id=kwargs['pk'])
            Comment.objects.create(**comment_form.cleaned_data)
            return HttpResponseRedirect('/news/' + str(kwargs['pk']))


class NewsFormView(View):
    def get(self, request):
        news_form = NewsForm()
        return render(request, 'app_news/news_create.html', context={'news_form': news_form})

    def post(self, request):
        news_form = NewsForm(request.POST)

        if news_form.is_valid():
            News.objects.create(**news_form.cleaned_data)
            return HttpResponseRedirect('/news/')
        return render(request, 'app_news/news_create.html', context={'news_form': news_form})


class NewsEditFormView(View):
    def get(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = NewsForm(instance=news)
        return render(request, 'app_news/news_edit.html', context={'news_form': news_form,
                                                                   'news_id': news_id})

    def post(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = NewsForm(request.POST, instance=news)

        if news_form.is_valid():
            news.save()
            return HttpResponseRedirect('/news/')
        return render(request, 'app_news/news_edit.html', context={'news_form': news_form,
                                                                   'news_id': news_id})
