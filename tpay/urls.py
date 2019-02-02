from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include([
        url(r'^v1/', include([
            url(r'^accounts/', include('accounts.urls')),
        ]))
    ])),
]
