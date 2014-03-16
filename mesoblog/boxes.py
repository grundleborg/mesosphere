# This file contains the functions for MesoBoxes
# See mesobox/boxes.py for the enabling code.
from mesoblog.models import Category

BOX_INCLUDES = (
        'categories',
)

def categories(request):
    c = Category.objects.all().order_by('name')
    return { "boxes": {"left": ['mesoblog/boxes/category-list.html',]}, "context": {"all_categories": c}}

