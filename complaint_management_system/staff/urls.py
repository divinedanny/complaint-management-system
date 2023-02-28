from django.urls import path
from .views import RegisterUserView, LoginUserView, LogoutUserView, UpdateUserView, UserListAllView, VerifyUserView, PasswordResetView, ForgotPasswordView

urlpatterns = [
    # path('register/',RegisterUserView.as_view(), name= 'register-user'),
    path('register/',RegisterUserView.as_view(), name= 'register-user'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/<uuid:uuid_param>/', LogoutUserView.as_view(), name='logout'),
    path('user-profile/', UpdateUserView.as_view(), name='update'),
    path('users/', UserListAllView.as_view(),name='users'),
    path('verify-user/',VerifyUserView.as_view(), name='verify-user'),
    path("request-reset-password/", ForgotPasswordView.as_view(), name="reset-password"),
    path('password-reset/<uidb64>/<token>/', PasswordResetView.as_view(), name='password-reset-confirmed')
    ]