from djangopro.modules import facade


def sort_modules(request):
    return {'MODULES': facade.list_modules_orderly()}
