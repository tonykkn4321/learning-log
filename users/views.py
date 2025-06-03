from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """注冊新用戶。"""
    if request.method != 'POST':
        # 顯示空的注冊表單。
        form = UserCreationForm()
    else:
        # 處理填寫好的表單。
        form = UserCreationForm(data=request.POST)
    
        if form.is_valid():
            new_user = form.save()
            # 讓用戶自動登錄，再重定向到主頁。
        login(request, new_user)
        return redirect('learning_logs:index')

    # 顯示空表單或指出表單無效。
    context = {'form': form}
    return render(request, 'registration/register.html', context)