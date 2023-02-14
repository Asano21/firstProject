from django.urls import path
from . import views
urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('about/', views.aboutPage, name='aboutPage'),
    path('hero/', views.heroPage, name='heroPage'),
    path('post/views/<int:pk>', views.postDetail, name='postDetail'),
    path('hero/views/<int:pk>', views.heroDetail, name='heroDetail')
]