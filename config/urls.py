from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    url(r'^api/', include([
        url(r'^v1/', include([
            url(r'^accounts/', include('accounts.urls')),
            url(r'^merchants/', include('merchants.urls')),
            url(r'^checkouts/', include('checkouts.urls')),
        ]))
    ])),
]
