from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
        path('transactions/', views.TransactionListCreateView.as_view(), name='transaction-list-create'),
        path('transactions/<uuid:id>/', views.TransactionRetrieveUpdateDestroyView.as_view(), name='transaction-detail'),
    ]