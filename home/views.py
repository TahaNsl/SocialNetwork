from django.shortcuts import render
from django.views import View

from posts.forms import PostSearchForm
from posts.models import Post


class HomeView(View):
    form_class = PostSearchForm
    home_template = 'home/index.html'

    def get(self, request):
        posts = Post.objects.all()
        if request.GET.get('search'):
            posts = posts.filter(body__contains=request.GET['search'])
        return render(request, 'home/index.html', {'posts': posts, 'form': self.form_class})
