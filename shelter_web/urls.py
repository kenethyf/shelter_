"""shelter_web URL Configuration

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
from shelter_dashboard.views import dashboard, home, unburden, index, login, password, indicadores, chat, config, eventos, treinamento

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name='login'),
    path('login/', login, name='login'),
    path('index/', index, name='index'),
    path('indicadores/', indicadores, name='indicadores'),
    path('chat/', chat, name='chat'),
    path('configuracoes/', config, name='configurações'),
    path('eventos/', eventos, name='eventos'),
    path('treinamentos/', treinamento, name='treinamentos'),
    # path('dashboard/', dashboard, name='dashboard'),
    # path('unburden/', unburden, name='unburden'),
]
