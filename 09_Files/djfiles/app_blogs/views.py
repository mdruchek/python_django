from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, FormMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog
from .forms import UploadFileForm


class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    ordering = ['-created']


class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog'


class CreateBlogView(LoginRequiredMixin, CreateView, FormMixin):
    model = Blog
    fields = 'content', 'image


def upload_blog_csv(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['file'].read()
            csv_str = file.decode('utf-8').split('\n')
            csv_reader = reader(csv_str, delimiter=',', quotechar='"')
            for row in csv_reader:
                blog = Blog.create(content=row[0], created=row[1])
            return reverse('app_blogs:upload_file_csv')
        else:
            form=UploadFileForm()
        context={
            'form': form
        }
        return render(request, 'app_blogs/upload_blog_csv.html', context=context)

