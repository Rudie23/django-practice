from djangopro.modules import facade


def sort_modulos(request):
    return {'MODULES': facade.list_modules_orderly()}
