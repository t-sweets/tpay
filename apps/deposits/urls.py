from django.conf.urls import url
from .views import DepositView


urlpatterns = [
    url(r'^$', DepositView.as_view()),
]