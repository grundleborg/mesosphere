# This file contains the functions for MesoBoxes
# See mesobox/boxes.py for the enabling code.
from mesoblog.models import Article, Category

import calendar

BOX_INCLUDES = (
        'categories',
        'dates',
)

def categories(request):
    result = {}
    if request.resolver_match.app_name is "mesoblog":
        c = Category.objects.all().order_by('name')
        result = { "boxes": {"left": ['mesoblog/boxes/category-list.html',]}, "context": {"all_categories": c}}

    return result

class ArchiveMonth:
    def __init__(self, month):
        self.month = month
        self.name = calendar.month_name[month]
        self.count = 0
        self.nameNumber = str(month).zfill(2)

    def inc(self):
        self.count = self.count + 1

class ArchiveYear:
    def __init__(self, year):
        self.year = year
        self.name =  str(year).zfill(4)
        self.months = []
        for n in range(1,12):
            self.months.append(ArchiveMonth(n))

    def __eq__(self, other):
        return self.year == other

def dates(request):
    result = {}
    if request.resolver_match.app_name is "mesoblog":
        articles = Article.objects.all().order_by("-date_published")

        d = {}
        for a in articles:
            year = None
            for y in d.values():
                if y.year == a.date_published.year:
                    year = y
                    break
            if year is None:
                year = ArchiveYear(a.date_published.year)

            month = year.months[a.date_published.month-1]
            month.inc()
            year.months[a.date_published.month-1] = month

            d[a.date_published.year] = year

        d = d.values()

        result = { "boxes": {"right": ['mesoblog/boxes/dates-list.html',]}, "context": {"dates": d}}

    return result

