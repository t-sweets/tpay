from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from .views import AccountRegisterView, AccountViewSet, IdmView, AccountCheckoutViewSet


urlpatterns = [
    url(r'^login/', obtain_jwt_token),
    url(r'^register/$', AccountRegisterView.as_view()),

    url(r'^profile/$', AccountViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'})),

    url(r'^idm/$', IdmView.as_view({'post': 'create',
                                    'get': 'list',
                                    'put': 'update',
                                    'delete': 'destroy',
                                    'patch': 'partial_update'})),

    url(r'^checkouts/$', AccountCheckoutViewSet.as_view({'get': 'list'})),
    url(r'^checkouts/(?P<id>.+)/$', AccountCheckoutViewSet.as_view({'get': 'retrieve'})),
]
