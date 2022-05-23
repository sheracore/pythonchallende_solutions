from django.http import HttpResponse
from django.template import loader
from django.views.generic.base import TemplateView
from django.utils.translation import gettext as _


def poll(request):
    template = loader.get_template('polls/index.html')
    context = {
        'template': template
    }
    return HttpResponse(template.render(context, request))

def gettext(TemplateView):
    return HttpResponse(_('I am wrapped by gettext or i am in gettext method'))
