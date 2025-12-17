from django.views import View
from django.db.models import F
from django.shortcuts import render, redirect, get_object_or_404

from shortener.forms import ShortURLForm
from shortener.models import ShortURL

class HomeView(View):
    def get(self, request):
        short_urls = ShortURL.objects.all()
        context = {
            'short_urls': short_urls,
            'form': ShortURLForm,
        }
        return render(
            request,
            'home.html',
            context
        )

class ShortURLCreateView(View):
    def post(self, request):
        form = ShortURLForm(request.POST)
        if form.is_valid():
            # 사용자에게 받은 form에는 original_url 밖에 없음
            obj = form.save(commit=False)   # 객체만 생성하고, 저장은 안 함
            while True:
                code = ShortURL.generate_code()
                if not ShortURL.objects.filter(code=code).exists():
                    break
            obj.code = code
            obj.save()
        return redirect('home')

class RedirectView(View):
    def get(self, request, code):
        short_url = get_object_or_404(ShortURL, code=code)
        short_url.access_count = F('access_count') + 1
        short_url.save()
        return redirect(short_url.original_url)

    def delete(self, request, code):
        short_url = get_object_or_404(ShortURL, code=code)
        short_url.delete()
        return redirect('home')