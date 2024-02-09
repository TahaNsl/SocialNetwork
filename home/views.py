from django.shortcuts import render
from django.views import View


class HomeView(View):
    home_template = 'home/index.html'

    def get(self, request):
        return render(request, self.home_template)
