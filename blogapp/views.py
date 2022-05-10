from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from blogapp.models import Blog, Comment
from blogapp.forms import BlogCreateForm
# Create your views here.


class HomeView(LoginRequiredMixin, ListView):
    login_url = '/account/login/'
    model = Blog

    template_name = 'blogapp/index.html'
    context_object_name = 'blogs'
    ordering = ['-dateCreated', '-id']

    def get_queryset(self):
        querySet = super().get_queryset()
        return querySet[:10]


class AllPostsView(LoginRequiredMixin, ListView):
    login_url = '/account/login/'
    model = Blog

    template_name = 'blogapp/allPosts.html'
    context_object_name = 'blogs'
    ordering = ['-dateCreated', '-id']


class PostDetailView(LoginRequiredMixin, DetailView):
    login_url = '/account/login/'
    model = Blog

    template_name = 'blogapp/postDetail.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        blog = self.get_object()
        user = self.request.user
        hasLiked = blog.likes.filter(username=user.username).exists()
        context['likedByMe'] = hasLiked
        return context

    def post(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        user = request.user

        if 'likePost' in request.POST:
            if user in blog.likes.all():
                blog.likes.remove(user)
            else:
                blog.likes.add(user)
            blog.save()

        else:
            comment = request.POST['comment']
            newComment = Comment(comment=comment, blog=blog, user=user)
            newComment.save()

        return HttpResponseRedirect(reverse('main:postDetail', args=[pk]))


class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = BlogCreateForm
    template_name = 'blogapp/createPost.html'

    def get_success_url(self):
        id = self.request.user.id
        return reverse('auth:account', args=[id])

    def form_valid(self, form):
        self.object = form.save()
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


