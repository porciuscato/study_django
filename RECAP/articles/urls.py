from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # path의 return 값은? 
    path('', views.index, name='index'),
    # rest api로 만들려고 해도 detail,과 create의 url이 겹친다.
    # path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    
]