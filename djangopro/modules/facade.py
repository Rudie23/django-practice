from typing import List

from djangopro.modules.models import Module, Lesson


def list_modules_orderly() -> List[Module]:
    """
    Sorted modules by titles
    :return:
    """
    return list(Module.objects.order_by('order').all())


def find_module(slug: str) -> Module:
    return Module.objects.get(slug=slug)


def lessons_ordered(module: Module):
    return list(module.lesson_set.order_by('order').all())


def find_lesson(slug):
    return Lesson.objects.select_related('module').get(slug=slug)

# def lista_aulas_de_modulo_ordenadas(module: Module):
#     return list(module.aula_set.order_by('order').all())


# def encontrar_aula(slug):
#     return Aula.objects.select_related('modulo').get(slug=slug)
#
#
# # O select_related só funciona quando você está no lado N do relacionameno e quer fazer o join com o lado 1 do
# # relacionamento
#
#
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
