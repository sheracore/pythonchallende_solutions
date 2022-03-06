from django.urls import path

from poll.views import poll

urlpatterns = [
    path('', view=poll, name='poll')
]