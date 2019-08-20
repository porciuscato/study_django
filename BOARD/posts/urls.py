from django.urls import path
from . import views

# 고유한 네임스페이스를 가짐
app_name = 'posts'

urlpatterns = [
    path('new/', views.new, name='new'), # 어플리케이션마다 이름 공간을 나눠서 쓰게 된다. 
    # posts_new 라고 하게 되면... 접두어 붙이는 게 좀 빡침
    # 네임스페이스를 분리!
    path('create/',views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
]