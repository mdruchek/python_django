from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import (CreateView,
                                  ListView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView)
from django.http.response import HttpResponseRedirect, HttpResponseForbidden
from django.views.generic.edit import ModelFormMixin
from django.urls import reverse_lazy, reverse
from .models import NewsModel, CommentModel
from .forms import CommentForm


class NewsListView(ListView):
    queryset = NewsModel.objects.filter(archived=False, published=True)
    template_name = 'app_news/news_list.html'
    context_object_name = 'news'

    def post(self, request, **kwargs):
        for key in request.POST.keys():
            if not key.startswith('csrf'):
                news_iter = NewsModel.objects.get(pk=key)
                news_iter.published = True
                news_iter.save()
        return redirect(reverse("app_news:list"))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unpublished_news'] = NewsModel.objects.filter(archived=False, published=False)
        context['archive_news'] = NewsModel.objects.filter(archived=True)
        return context


class NewsDetailViews(ModelFormMixin, DetailView):
    queryset = NewsModel.objects.filter(archived=False, published=True)
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


class NewsCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'app_news.add_newsmodel'
    login_url = 'app_users:login'
    model = NewsModel
    template_name = 'app_news/news_create.html'
    fields = 'title', 'content_news'
    success_url = reverse_lazy('app_news:list')
    login_url = 'app_users:login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'app_news.change_newsmodel'
    login_url = 'app_users:login'
    model = NewsModel
    fields = 'title', 'content_news'
    template_name = 'app_news/news_update.html'
    context_object_name = 'news'

    def get_success_url(self):
        return reverse('app_news:details', kwargs={'pk': self.object.pk})

    def get(self, request, *args, **kwargs):
        author = NewsModel.objects.get(pk=kwargs['pk']).author.username
        if author != request.user.username:
            return HttpResponseForbidden()
        return super().get(request, *args, **kwargs)


class NewsArchivedView(PermissionRequiredMixin, DeleteView):
    permission_required = 'app_news.delete_newsmodel'
    login_url = 'app_users:login'
    model = NewsModel
    template_name = 'app_news/news_archived.html'
    context_object_name = 'news'

    def form_valid(self, form):
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(reverse('app_news:list'))


class MainView(View):

    def get(self, request):
        return render(request, 'app_news/main.html')
