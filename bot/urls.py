from django.conf.urls import url
from .views import ChatterBotApiView

urlpatterns = [
    url(r'^$', ChatterBotApiView.as_view(), name='main'),
]
