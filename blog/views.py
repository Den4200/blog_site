from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import redirect, render
from django.views import View
from markdownx.utils import markdownify

from blog.forms import CreatePostForm
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
        form = CreatePostForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CreatePostForm(request.POST)

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
