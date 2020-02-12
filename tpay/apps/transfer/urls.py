from django.conf.urls import url
from .views import TransferView


urlpatterns = [
    url(r'^$', TransferView.as_view()),
]
