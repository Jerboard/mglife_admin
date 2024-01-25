from django.contrib import admin
from django.urls import path

from admin_bot.views import api_view

urlpatterns = [
    path('api/v1/update_users', api_view),
    path('admin/', admin.site.urls),
]
