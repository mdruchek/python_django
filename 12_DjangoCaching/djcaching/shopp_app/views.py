from django.shortcuts import render


def main_page_view(request):
    return render(request, 'shopp_app/index.html')
