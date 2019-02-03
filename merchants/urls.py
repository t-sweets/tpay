from django.conf.urls import url

from .views import MerchantViewSet, MerchantAllCheckoutListView, MerchantCheckoutListView


urlpatterns = [
    url(r'^checkouts/$', MerchantAllCheckoutListView.as_view()),
    url(r'^(?P<uuid>.+)/checkouts/$', MerchantCheckoutListView.as_view()),
    url(r'^(?P<uuid>.+)/$', MerchantViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    url(r'^$', MerchantViewSet.as_view({'get': 'list'})),
]
