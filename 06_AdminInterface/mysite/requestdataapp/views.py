from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import UserBioForm, UploadFileForm


def process_get_view(request: HttpRequest) -> HttpResponse:
    print(request.GET['name'])
    context = {

    }
    return render(request, 'requestdataapp/request-query-params.html', context=context)


def user_form(request: HttpRequest) -> HttpResponse:
    context = {
        'form': UserBioForm(),
    }
    return render(request, 'requestdataapp/user-bio-form.html', context=context)


def handle_file_upload(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            myfile = form.cleaned_data['file']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            print('Файл {file_name} сохранён'.format(file_name=filename))
    else:
        form = UploadFileForm()

    context = {
        'form': form
    }

    return render(request,
                  'requestdataapp/file-upload.html',
                  context=context)
