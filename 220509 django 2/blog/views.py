from django.shortcuts import render,redirect
from .models import Post
import datetime
# Create your views here.

count = 0

def index(request):
    global count
    count = count+1
    
    return render(request, "blog/index.html", 
                  {
                      "msg":"헬로! 장고 프레임워크",
                      "count":count
                   })
    
#=============================================================
# blog용 함수들
def blog_main(request):
    return render(request, "blog/main.html")

def blog_create(request):
    if request.method == 'POST':
        post_data = request.POST
        data = Post(title=post_data.get('title'),content=post_data.get('content'),created_at=datetime.datetime.now(),updated_at=datetime.datetime.now())
        data.save()
        return redirect('main')
    return render(request, "blog/create.html")

# 리스트
def blog_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'posts':posts})

# 수정
def blog_update(request, pk):
    if request.method == 'POST':
        post_data = request.POST
        
        my_post = Post.objects.get(id=pk)
        my_post.title = post_data.get('title')        
        my_post.content = post_data.get('content')        
        my_post.updated_at = datetime.datetime.now()        
        my_post.save()        
        return redirect('list')
    else:
        my_post = Post.objects.get(id=pk)
        return render(request,'blog/update.html',{'post':my_post})
    
# 삭제
def blog_delete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('list')