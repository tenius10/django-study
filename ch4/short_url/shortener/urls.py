from django.urls import path
from shortener import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('short-urls/', views.ShortURLCreateView.as_view(), name='shorten_url'),
    path('<str:code>', views.RedirectView.as_view(), name='short_url_detail'),
]