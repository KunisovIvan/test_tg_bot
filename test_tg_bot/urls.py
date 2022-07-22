from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('tg_bot.urls')),
    path('admin/', admin.site.urls),
]
