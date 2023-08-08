"""
URL configuration for hw1_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from t1.views import plus, do_upper, check_palindrome, calculator
urlpatterns = [
    path('admin/', admin.site.urls),
    path("nfactorial/", include("t1.urls")),
    path("<int:first>/add/<int:second>/", plus, name="plus"),
    path("transform/<str:text>/", do_upper, name="upper"),
    path("check/<str:word>/", check_palindrome, name="check_palindrome"),
    path("calc/<int:first>/<str:operation>/<int:second>/", calculator, name="calculator")
]
