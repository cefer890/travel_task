from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CustomerSerializer, CustomerAndPasportCreateSerializer, PassportSerializer
from ..models import CustomerInformations, PassportInformations


class CustomerAndPassportCreateView(generics.CreateAPIView):
    "API View that receives POST with project returns transaction ID to pass to the next step."
    queryset = PassportInformations.objects.all()
    serializer_class = CustomerAndPasportCreateSerializer
    name = 'customer-and-passport-create'


class CustomerList(generics.ListAPIView):
    "API View that receives GET returns the list of projects."
    queryset = CustomerInformations.objects.all()
    serializer_class = CustomerSerializer
    name = 'customer-list'


class PassportList(generics.ListAPIView):
    "API View that receives GET returns the list of projects."
    queryset = PassportInformations.objects.all()
    serializer_class = PassportSerializer
    name = 'passport-list'


class CustomerUpdateView(generics.UpdateAPIView):
    queryset = CustomerInformations.objects.all()
    serializer_class = CustomerSerializer
    name = 'customer-update'


class PassportUpdateView(generics.UpdateAPIView):
    queryset = PassportInformations.objects.all()
    serializer_class = PassportSerializer
    name = 'passport-update'


class PassportDeleteView(generics.DestroyAPIView):
    queryset = PassportInformations.objects.all()
    serializer_class = PassportSerializer
    name = 'passport-delete'


class CustomerDeleteView(generics.DestroyAPIView):
    queryset = CustomerInformations.objects.all()
    serializer_class = CustomerSerializer
    name = 'customer-delete'
