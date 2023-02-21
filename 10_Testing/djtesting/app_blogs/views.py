from _csv import reader
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog, BlogImage
from .forms import UploadFileForm, BlogCreateForm


class BlogListView(ListView):
    model = Blog
    template_name = 'app_blogs/list.html'
    context_object_name = 'blogs'
    ordering = ['-created']


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'app_blogs/detail.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = kwargs['object'].blogimage_set.all()
        return context


class BlogCreateView(LoginRequiredMixin, CreateView):
    login_url = 'app_users:login'
    form_class = BlogCreateForm
    model = BlogImage
    template_name = 'app_blogs/create.html'
    success_url = reverse_lazy('app_blogs:list')

    def post(self, request, *args, **kwargs):
        form = BlogCreateForm(request.POST, request.FILES)

        blog = Blog.objects.create(content=self.request.POST['content'],
                                   author=self.request.user)
        form.instance.blog = blog

        if form.is_valid():
            images = request.FILES.getlist('image')
            for img in images:
                instance = BlogImage(image=img, blog=blog)
                instance.save()
            return HttpResponseRedirect(reverse('app_blogs:list'))


def upload_blog_csv(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['file_csv'].read()
            csv_str = csv_file.decode('utf-8').split('\n')
            csv_reader = reader(csv_str, delimiter=',', quotechar='"')
            for row in csv_reader:
                if row:
                    Blog.objects.create(content=row[0], created=row[1], author=request.user)
            return HttpResponseRedirect(reverse('app_blogs:list'))
    else:
        form = UploadFileForm()
    context = {
        'form': form
    }
    return render(request, 'app_blogs/upload_file_csv.html', context=context)


class BlogDeleteView(DeleteView):
    model = Blog
