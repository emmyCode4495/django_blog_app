from django.shortcuts import render,get_object_or_404

# Adding the pagination classes
from django.core.paginator import (Paginator,
                                    EmptyPage, 
                                    PageNotAnInteger)

from .models import Post

def post_list(request):

    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)# declaring number of post per page
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    context = {'posts':posts,
                'page':page}

    
    context = {'posts':posts}
    return render(request,'posts/list.html',context)

def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post,
                            slug = post,
                            status = 'published',
                            publish__year = year,
                            publish__month = month,
                            publish__day = day)

    context = {'post':post}
    return render(request, 'posts/detail.html',context)

