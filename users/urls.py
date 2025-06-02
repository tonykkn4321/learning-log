"""為應用程序users定義URL模式。"""

from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # 包含默認的身份驗證URL。
    path('', include('django.contrib.auth.urls')),
]