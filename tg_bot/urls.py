from django.urls import path

from tg_bot.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
