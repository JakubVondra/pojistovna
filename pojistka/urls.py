# urls.py
from django.urls import path
from .views import HomeView, SeznamUzivateluView, UzivatelDetailView, VytvoritPojistkuView
from . import views

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('vytvor_pojistence_form/', views.PridatPojistenceView.as_view(), name='vytvor_pojistence_form'),
    path('seznam_pojistencu/', SeznamUzivateluView.as_view(), name='seznam_pojistencu'),
    path('uzivatel/<int:pk>/', UzivatelDetailView.as_view(), name='uzivatel_detail'),
    path("register/", views.UzivatelViewRegister.as_view(), name="registrace"),
    path("login/", views.UzivatelViewLogin.as_view(), name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("vytvorit_pojistku/", VytvoritPojistkuView.as_view(), name="vytvorit_pojistku"),

    

]


