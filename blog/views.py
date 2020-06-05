from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import redirect, render
from django.views import View
from markdownx.utils import markdownify

from blog.forms import BlogPostForm
from blog.models import BlogPost


class IndexView(View):
    template_name = 'blog/index.html'

    def get(self, request):
        posts = BlogPost.objects.order_by('-created_at')

        for post in posts:
            post.content = markdownify(post.content)

        return render(request, self.template_name, {'posts': posts})


class CreatePostView(LoginRequiredMixin, View):
    template_name = 'blog/new_post.html'

    def get(self, request):
        form = BlogPostForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = BlogPostForm(request.POST)

        if not form.is_valid():
            messages.error(request, 'Invalid form', extra_tags='dnager')
            return render('create_post')

        post = form.save(commit=False)
        post.user = request.user
        post.save()

        return redirect('blog_post', post_id=post.id)


class BlogPostView(View):
    template_name = 'blog/blog_post.html'

    def get(self, request, post_id):
        try:
            blog_post = BlogPost.objects.get(id=post_id)
        except BlogPost.DoesNotExist:
            raise Http404('Blog post does not exist')
        else:
            blog_post.content = markdownify(blog_post.content)
            return render(request, self.template_name, {'blog_post': blog_post})


class UpdatePostView(LoginRequiredMixin, View):
    template_name = 'blog/update_post.html'

    def get(self, request, post_id):
        try:
            blog_post = BlogPost.objects.get(id=post_id)
        except BlogPost.DoesNotExist:
            raise Http404('Blog post does not exist')
        else:
            if request.user != blog_post.user:
                return HttpResponseForbidden('You are not allowed to edit this post')

            form = BlogPostForm(instance=blog_post)
            return render(request, self.template_name, {'form': form})

    def post(self, request, post_id):
        try:
            blog_post = BlogPost.objects.get(id=post_id)
        except BlogPost.DoesNotExist:
            raise Http404('Blog post does not exist')
        else:
            if request.user != blog_post.user:
                return HttpResponseForbidden('You are not allowed to edit this post')

            form = BlogPostForm(request.POST, instance=blog_post)
            form.save()

            messages.success(request, 'Post updated successfully')
            return redirect('blog_post', post_id=post_id)
