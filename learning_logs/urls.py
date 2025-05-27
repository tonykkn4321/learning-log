"""定義learning_logs的URL模式。"""
from django.urls import path
from . import views
app_name = 'learning_logs'
urlpatterns = [
    # 主頁
    path('', views.index, name='index'),
    # 顯示所有的主題。
    path('topics/', views.topics, name='topics'),
    # 特定主題的詳細頁面。
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]