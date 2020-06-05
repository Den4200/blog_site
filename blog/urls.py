from django.urls import path

from blog.views import BlogPostView, CreatePostView, DeletePostView, IndexView, UpdatePostView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/create/', CreatePostView.as_view(), name='create_post'),
    path('post/<int:post_id>/', BlogPostView.as_view(), name='blog_post'),
    path('post/<int:post_id>/update/', UpdatePostView.as_view(), name='update_post'),
    path('post/<int:post_id>/delete/', DeletePostView.as_view(), name='delete_post')
]
