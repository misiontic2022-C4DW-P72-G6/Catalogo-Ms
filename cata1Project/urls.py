"""cata1Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from cata1App import views

urlpatterns = [
    path('habitacion/', views.habitacionCreateView.as_view()),
    path('catalogo/', views.catalogoCreateView.as_view()),
    path('catalogo/<int:pk>/', views.catalogoDetailView.as_view()),
    path('habitacion/<int:pk>/', views.habitacionDetailView.as_view()),
]
