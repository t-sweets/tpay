from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include([
        url(r'^v1/', include([
            url(r'^accounts/', include('accounts.urls')),
            url(r'^merchants/', include('merchants.urls')),
            url(r'^checkouts/', include('checkouts.urls')),
            url(r'^deposits/', include('deposits.urls')),
            url(r'^media/', include('media_upload.urls')),
            url(r'^transactions/', include('transactions.urls')),
        ]))
    ])),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
