from django.urls import path
from . import views
# . 형제이기 때문에 현재 폴더에서 가져오겠다는 뜻의 점

urlpatterns = [
    path('new/', views.new),
    path('create/', views.create),
]