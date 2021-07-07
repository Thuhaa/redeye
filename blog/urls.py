from django.urls import path
from . import views

urlpatterns = [
path('', views.homepage, name='homepage'),
path('blog/', views.blog, name='blog'),
path('blog/<str:slug>/', views.post_detail, name='detail'),
path('about-us', views.about, name='about'),
path('contact-us', views.contact, name='contact'),
path('blog/category/budsolutionz/', views.potland, name='budsolutionz'),
path('blog/category/music/', views.music, name='music'),
path('blog/category/lifestyle/', views.lifestyle, name='lifestyle'),
path('feedback/', views.feedback, name='feedback')
]