from typing import List

from django.db.models import Prefetch

from djangopro.modules.models import Module, Lesson


def list_modules_orderly() -> List[Module]:
    """
    Sorted modules by titles
    :return:
    """
    return list(Module.objects.order_by('order').all())


def search_module(slug: str) -> Module:
    return Module.objects.get(slug=slug)


# Django will create an attribute in the side 1 of its relationship (Module) with N (Lessons),
# therefore it will be created a relation between many to one.
# Using o lesson_set, you can access all modules' lessons
def list_lessons_of_modules_sorted(module: Module):
    return list(module.lesson_set.order_by('order').all())


# relacionamento The select_related will fix the N+1 select issue. It just works when come from the side N and wants
# to make a join in relationship
def find_lesson(slug):
    return Lesson.objects.select_related('module').get(slug=slug)


# If you want to access the side 1 besides the N, you must use prefetch_related. It will not do a join, but a Query
# to search respective elements from side 1
# to_attrs attribute the name of Query that will contain the result.
def sort_modules_with_lessons():
    sorted_lessons = Lesson.objects.order_by('order')
    return Module.objects.order_by('order').prefetch_related(Prefetch
                                                             ('lesson_set', queryset=sorted_lessons,

                                                              to_attr='lessons')).all()
