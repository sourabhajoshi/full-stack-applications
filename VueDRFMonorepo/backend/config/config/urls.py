from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hello/', include('api.urls')),
    path('api/accounts/', include('accounts.urls')),
]
