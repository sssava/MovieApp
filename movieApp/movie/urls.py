from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home, name="home"),
    path('movie/<slug:slug>/', about, name="about"),
    path('category/<slug:slug>/', category, name="category"),
    path('search/', Search.as_view(), name="search"),
    path('register', register, name="register"),
    path('login/', login_page, name='login'),
    path('logout/', logout_user, name="logout"),
    path('user/', user_page, name="user"),
    path('like-movie/', likeMovie, name="like-movie"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='movie/password_reset.html'),
         name="reset_password"),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='movie/password_reset_sent.html'),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='movie/password_reset_form.html'),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='movie/password_reset_done.html'),
         name="password_reset_complete"),
]