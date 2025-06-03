"""為應用程序users定義URL模式。"""

from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # 包含默認的身份驗證URL。
    path('', include('django.contrib.auth.urls')),
    # 注冊頁面
    path('register/', views.register, name='register'),
]