from django.shortcuts import render
from rest_framework import generics

from .serializers import TransactionsSerializer
from .models import Transaction

# Create your views here.
class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionsSerializer

class TransactionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionsSerializer
    lookup_field = 'id'