from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from poll import views

urlpatterns = [
    path('polls', view=views.poll, name='poll'),
    path('gettext', view=views.gettext)
]

# urlpatterns += staticfiles_urlpatterns()