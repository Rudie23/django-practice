from typing import List

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
# therefore it will be created a realition between many to one.
# Using o lesson_set, you can access all modules' lessons
def list_lessons_of_modules_sorted(module: Module):
    return list(module.lesson_set.order_by('order').all())


# O select_related só funciona quando você está no lado N do relacionameno e quer fazer o join com o lado 1 do relacionamento
def find_lesson(slug):
    return Lesson.objects.select_related('module').get(slug=slug)

# def listar_modulos_com_aulas():
#     aulas_ordenadas = Aula.objects.order_by('order')
#     return Module.objects.order_by('order').prefetch_related(Prefetch
#                                                              ('aula_set', queryset=aulas_ordenadas,
#
#                                                               to_attr='aulas')).all()
#
# # Quando você sai do lado 1 do relacionamento, e quer acessar o lado n do relacionameno você usa o prefetch_related.
# Ele não vai fazer um join no BD, ele vai fazer uma Query para buscar os elementos respectivos ao lado 1, neste caso o
# # módulo, depois ele vai fazer uma Query para buscar as aulas.
# #
# # o to_attrs contém o nome do atributo a ser utilizado pelo modulo que vai conter o resultado
