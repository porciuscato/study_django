"""first_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    # path 함수는 
    # 첫번째 인자 : 주문서(url 경로)
    # 두번째 인자 : view 함수의 위치
    path('admin/', admin.site.urls),
    # pages 앱 안에 있는 index를 찾아가라
    path('index/', views.index),
    # 장고는 trailing comma를 붙이는 것이 컨벤션. 지금까지는 안 썼음
    path('home/',views.home),
    path('lotto/',views.lotto),
    path('cube/<int:num>/', views.cube),
    path('match/',views.match),
]