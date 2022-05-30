from django.urls import path
from . import views


urlpatterns = [
    path('customer-and-passport-create/',
         views.CustomerAndPassportCreateView.as_view(),
         name=views.CustomerAndPassportCreateView.name),
    path('customer-list/',
         views.CustomerList.as_view(),
         name=views.CustomerList.name),
    path('passport-list/',
         views.PassportList.as_view(),
         name=views.PassportList.name),
    path('customer-update/<int:pk>/',
         views.CustomerUpdateView.as_view(),
         name=views.CustomerUpdateView.name),
    path('passport-update/<int:pk>/',
         views.PassportUpdateView.as_view(),
         name=views.PassportUpdateView.name),
    path('passport-delete/<int:pk>/delete/',
         views.PassportDeleteView.as_view(),
         name=views.PassportDeleteView.name),
    path('customer-delete/<int:pk>/delete/',
         views.CustomerDeleteView.as_view(),
         name=views.CustomerDeleteView.name),
]