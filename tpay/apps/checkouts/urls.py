from django.conf.urls import url
from .views import CheckoutView


urlpatterns = [
    url(r'^(?P<pk>.+)/$', CheckoutView.as_view({'delete': 'destroy'})),
    url(r'^$', CheckoutView.as_view({'post': 'create'})),
]
