from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from poll.views import poll

urlpatterns = [
    path('', view=poll, name='poll')
]

# urlpatterns += staticfiles_urlpatterns()