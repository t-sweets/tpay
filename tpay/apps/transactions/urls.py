from django.conf.urls import url
from .views import TransactionViewSet


urlpatterns = [
    url(r'^$', TransactionViewSet.as_view({'get': 'list'})),
]
