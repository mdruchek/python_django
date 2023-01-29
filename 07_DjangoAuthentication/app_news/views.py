from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView,
                                  ListView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView)
from django.http.response import HttpResponseRedirect
from django.views.generic.edit import ModelFormMixin
from .models import NewsModel, CommentModel
from django.urls import reverse_lazy, reverse
from .forms import CommentForm


class NewsListView(ListView):
    queryset = NewsModel.objects.filter(archived=False)
    template_name = 'app_news/news_list.html'
    context_object_name = 'news'


class NewsDetailViews(ModelFormMixin, DetailView):
    queryset = NewsModel.objects.filter(archived=False)
    template_name = 'app_news/news_details.html'
    context_object_name = 'news'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = kwargs['object'].commentmodel_set.all()
        return context

    def post(self, request, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.cleaned_data['news'] = NewsModel.objects.get(id=kwargs['pk'])
            comment_form.cleaned_data['user'] = request.user
            CommentModel.objects.create(**comment_form.cleaned_data)
            return HttpResponseRedirect(reverse('app_news:details', kwargs={'pk': kwargs['pk']}))


class NewsCreateView(LoginRequiredMixin, CreateView):
    model = NewsModel
    template_name = 'app_news/news_create.html'
    fields = 'title', 'content_news'
    success_url = reverse_lazy('app_news:list')
    login_url = 'app_users:login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NewsUpdateView(UpdateView):
    model = NewsModel
    fields = 'title', 'content_news'
    template_name = 'app_news/news_update.html'
    context_object_name = 'news'

    def get_success_url(self):
        return reverse('app_news:details', kwargs={'pk': self.object.pk})


class NewsArchivedView(DeleteView):
    model = NewsModel
    template_name = 'app_news/news_archived.html'
    context_object_name = 'news'

    def form_valid(self, form):
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(reverse('app_news:list'))
