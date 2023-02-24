from django.urls import path
from .views import RegisterUserView, LoginUserView, LogoutUserView, UpdateUserView, UserListAllView, VerifyUserView

urlpatterns = [
    # path('register/',RegisterUserView.as_view(), name= 'register-user'),
    path('register/',RegisterUserView.as_view(), name= 'register-user'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/<uuid:pk/', LogoutUserView.as_view(), name='logout'),
    path('user-profile/', UpdateUserView.as_view(), name='update'),
    path('users/', UserListAllView.as_view(),name='users'),
    path('verify-user/',VerifyUserView.as_view(), name='verify-user'),
    ]




