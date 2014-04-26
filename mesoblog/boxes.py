# This file contains the functions for MesoBoxes
# See mesobox/boxes.py for the enabling code.
from mesoblog.models import Article, Category

from datetime import date

import calendar
import functools

BOX_INCLUDES = (
        'categories',
        'archive',
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

@functools.total_ordering
class ArchiveYear:
    def __init__(self, year):
        self.year = year
        self.name =  str(year).zfill(4)
        self.months = []
        for n in range(1,12):
            self.months.append(ArchiveMonth(n))

    def __eq__(self, other):
        return self.year == other

    def __lt__(self, other):
        if self.year < other.year:
            return True
        else:
            return False

def archive(request):
    result = {}
    if request.resolver_match.app_name is "mesoblog":
        articles = Article.objects.all()
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

        d = sorted(d.values(), reverse=True)

        result = { "boxes": {"right": ['mesoblog/boxes/archive-list.html',]},
                   "context": {"archive_dates": d,
                               "archive_current_year": str(date.today().year),
                              }
                 }

    return result

