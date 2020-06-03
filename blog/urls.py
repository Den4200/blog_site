from django.urls import path

from blog.views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='index')
]
