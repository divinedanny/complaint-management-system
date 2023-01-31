from django.urls import path
from .views import ComplainCreateView,ComplainEditView,ComplainListAllView,ComplainDeleteView

urlpatterns =[
    path('', ComplainCreateView.as_view(), name='create-complain'),
    path('history/<int:pk>/', ComplainEditView.as_view(), name='edit-complain'),
    path('history/', ComplainListAllView.as_view(), name='history-comaplain'),
    path('delete/<int:pk>/', ComplainDeleteView.as_view(), name='delete-complain'),
]