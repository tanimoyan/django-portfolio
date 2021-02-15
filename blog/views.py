from django.shortcuts import render, redirect
from .models import Image, Post
from .forms import ImageForm, PostForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

def showall(request):
    images = Image.objects.all()
    posts = Post.objects.all()
    return render(request, 'blog/showall.html', {'images':images, 'posts':posts})

def upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:showall')
    else:
        form = ImageForm()

    context = {'form':form}
    return render(request, 'blog/upload.html', context)
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

    
# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     posts = Post.objects.all()
#     return render(request, 'blog/showall.html', {'posts':posts})