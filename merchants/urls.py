from django.conf.urls import url
from .views import MerchantViewSet, MerchantAllCheckoutListView, MerchantCheckoutListView


urlpatterns = [
    url(r'^checkout/', MerchantAllCheckoutListView.as_view()),
    url(r'^(?P<merchant>.+)/checkout/$', MerchantCheckoutListView.as_view()),
]
