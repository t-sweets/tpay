from django.conf.urls import url
from rest_framework_jwt.views import (obtain_jwt_token, refresh_jwt_token,
                                      verify_jwt_token)
from .views import AuthRegister, AuthInfoGetView, AuthInfoUpdateView, AuthInfoDeleteView


urlpatterns = [
    url(r'^login/', obtain_jwt_token),
    url(r'^register/$', AuthRegister.as_view()),
    url(r'^profile/$', AuthInfoGetView.as_view()),
    url(r'^update/$', AuthInfoUpdateView.as_view()),
    url(r'^delete/$', AuthInfoDeleteView.as_view()),
    url(r'^list/$', AuthInfoDeleteView.as_view()),
]
