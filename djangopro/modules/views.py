from django.shortcuts import render

from djangopro.modules import facade


# Create your views here.

def detail(request, slug):
    module = facade.find_module(slug)
    lessons = facade.lessons_ordered(module)
    return render(request, 'modules/module_detail.html', {'module': module, 'lessons': lessons})


def lesson(request, slug):
    lesson = facade.find_lesson(slug)
    return render(request, 'modules/lesson_detail.html', {'lesson': lesson})
