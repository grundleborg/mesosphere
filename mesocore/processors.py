from django.conf import settings
from django.core.urlresolvers import reverse

def settings_context_processor(request):
    return settings.CONTEXT_ADDITIONS;

class NavItem:
    def __init__(self, name, url, active=False):
        self.name = name
        self.url = url
        self.active=active

def navigation_context_processor(request):
    
    return {'nav': [
        NavItem("Home",reverse('mesohome.views.index'),True if request.resolver_match.app_name is "mesohome" else False),
        NavItem("Blog",reverse('mesoblog.views.index'),True if request.resolver_match.app_name is "mesoblog" else False),
    ]}


