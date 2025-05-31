from django.shortcuts import render
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

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

def new_topic(request):
    """添加新主題。"""

    if request.method != 'POST':
        # 未提交數據：創建一個新表單。
        form = TopicForm()
    else:
        # POST提交的數據：對數據進行處理。
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    # 顯示空表單或指出表單數據無效。
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """在特定主題中添加新條目。"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # 未提交數據：創建一個空表單。
        form = EntryForm()
    else:
        # POST提交的數據：對數據進行處理。
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # 顯示空表單或指出表單數據無效。
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
    """編輯既有條目。"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # 初次請求：使用當前條目填充表單。
        form = EntryForm(instance=entry)
    else:
        # POST提交的數據：對數據進行處理。
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
            
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)