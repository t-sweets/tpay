from django.conf.urls import url

from .views import MerchantViewSet, MerchantAllCheckoutListView, MerchantCheckoutListView


urlpatterns = [
    url(r'^', MerchantViewSet.as_view({'get': 'list'})),
    url(r'^(?P<merchant>.+)/$', MerchantViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    url(r'^checkout/$', MerchantAllCheckoutListView.as_view()),
    url(r'^(?P<merchant>.+)/checkout/$', MerchantCheckoutListView.as_view()),
]
