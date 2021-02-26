from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect

from posts.models import Post
from posts.forms import PostForm


# Create your views here.


def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, 'Successfully created')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'title': 'Create',
        'form': form
    }
    return render(request, 'post_form.html', context)


def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        'title': 'Detail',
        'post': instance
    }
    return render(request, 'post_detail.html', context)


def posts_list(request):
    queryset = Post.objects.all()

    query = request.GET.get('q')

    if query:
        queryset = queryset.filter(title__icontains=query)

    paginator = Paginator(queryset, 5)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        'title': 'List',
        'objects_list': queryset,
        'page_request_var': page_request_var
    }
    return render(request, 'post_list.html', context)


def post_update(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, '<a href="#">Item</a> saved', extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'title': 'Detail',
        'post': instance,
        'form': form
    }

    return render(request, 'post_form.html', context)


def post_delete(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, 'Successfully deleted!')
    return redirect('posts:posts_list')