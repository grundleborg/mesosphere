# This file contains the functions for MesoBoxes
# See mesobox/boxes.py for the enabling code.
from mesoblog.models import Category

BOX_INCLUDES = (
        'categories',
)

def categories(request):
    result = {}
    if request.resolver_match.app_name is "mesoblog":
        c = Category.objects.all().order_by('name')
        result = { "boxes": {"left": ['mesoblog/boxes/category-list.html',]}, "context": {"all_categories": c}}

    return result

