from django.shortcuts import render

from djangopro.modules import facade


# Create your views here.

def detail(request, slug):
    module = facade.find_module(slug)
    return render(request, 'modules/module_detail.html', {'module': module})
