from django.http import HttpResponse
from django.template import loader


def poll(request):
    template = loader.get_template('polls/index.html')
    context = {
        'template': template
    }
    return HttpResponse(template.render(context, request))
