from django.shortcuts import render
from django.views import View


class IndexView(View):
    template_name = 'blog/index.html'

    def get(self, request):
        return render(request, self.template_name)
