from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("<int:pk>/", views.detail, name="detail"),
    path("list", views.list, name="list"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
]
