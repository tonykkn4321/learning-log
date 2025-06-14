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
    # 用於添加新主題的頁面。
    path('new_topic/', views.new_topic, name='new_topic'),
    # 用於添加新條目的頁面。
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # 用於編輯條目的頁面。
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]