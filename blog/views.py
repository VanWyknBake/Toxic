from functools import total_ordering
from django.shortcuts import get_object_or_404, render
from .models import Post
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

@login_required
def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, "blog/home.html", context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
    

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))


def DislikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.dislikes.add(request.user)
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))



def search_posts(request):
    if request.method == "POST":
        searched = request.POST['searched']
        posts = Post.objects.filter(uid__contains=searched)
        

        return render(request, 'blog/search_posts.html', {'searched': searched,'posts': posts})
    else:
        return render(request, 'blog/search_posts.html')

   


class UserPostListView(LoginRequiredMixin ,ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
        
    



class PostDetailView(LoginRequiredMixin ,DetailView):
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        total_dislikes = stuff.total_dislikes()
        context['total_dislikes'] = total_dislikes
        context["total_likes"] = total_likes
        return context
    
    
    
        




    


class PostCreateView(LoginRequiredMixin ,CreateView):
    model = Post
    fields = ['ign', 'uid', 'content', 'image']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin , UserPassesTestMixin ,UpdateView):
    model = Post
    fields = ['ign', 'uid', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, "blog/about.html", {'title':'About'})
