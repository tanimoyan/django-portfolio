from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.showall, name='showall'),
    # path('', views.upload, name='upload'),
    # path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/', views.showall, name='post_detail'),
]