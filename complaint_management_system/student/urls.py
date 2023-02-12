from django.urls import path
from .views import RegisterUserView, LoginUserView, LogoutUserView, UpdateUserView, UserListAllView

urlpatterns = [
    path('',RegisterUserView.as_view(), name= 'register-user'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/<uuid:pk/', LogoutUserView.as_view(), name='logout'),
    path('user-profile/<uuid:pk>/', UpdateUserView.as_view(), name='update'),
    path('users/', UserListAllView.as_view(),name='users'),
]