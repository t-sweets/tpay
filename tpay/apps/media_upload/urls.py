from django.conf.urls import url
from .views import ImageView


urlpatterns = [
    url(r'^upload/$', ImageView.as_view()),
]
