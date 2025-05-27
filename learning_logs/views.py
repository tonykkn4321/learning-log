from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    """學習筆記的主頁。"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """顯示所有的主題。"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """顯示單個主題及其所有的條目。"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)