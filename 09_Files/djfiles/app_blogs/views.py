from _csv import reader

from django.forms import Form
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog
from .forms import UploadFileForm


class BlogListView(ListView):
    model = Blog
    template_name = 'app_blogs/list.html'
    context_object_name = 'blogs'
    ordering = ['-created']


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'app_blogs/detail.html'
    context_object_name = 'blog'


class BlogCreateView(LoginRequiredMixin, CreateView):
    login_url = 'app_users:login'
    model = Blog
    template_name = 'app_blogs/create.html'
    fields = 'content', 'image'
    success_url = reverse_lazy('app_blogs:list')

    def form_valid(self, form: Form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def upload_blog_csv(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['file'].read()
            csv_str = csv_file.decode('utf-8').split('\n')
            csv_reader = reader(csv_str, delimiter=',', quotechar='"')
            for row in csv_reader:
                blog = Blog.create(content=row[0], created=row[1])
            return reverse('app_blogs:upload_file_csv')
        else:
            form = UploadFileForm()
        context = {
            'form': form
        }
        return render(request, 'app_blogs/upload_blog_csv.html', context=context)

