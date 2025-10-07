from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('nosotros/', views.AboutView.as_view(), name='about'),
    path('galeria/', views.GalleryView.as_view(), name='gallery'),
    path('preguntas-frecuentes/', views.FAQView.as_view(), name='faq'),
]