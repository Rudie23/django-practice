from django.shortcuts import render

from djangopro.modules import facade


# Create your views here.

def detail(request, slug):
    module = facade.search_module(slug)
    lessons = facade.list_lessons_of_modules_sorted(module)
    return render(request, 'modules/module_detail.html', {'module': module, 'lessons': lessons})


def lesson(request, slug):
    lesson = facade.find_lesson(slug)
    return render(request, 'modules/lesson_detail.html', {'lesson': lesson})


def index(request):
    ctx = {'modules': facade.sort_modules_with_lessons()}
    return render(request, 'modules/index.html', ctx)
