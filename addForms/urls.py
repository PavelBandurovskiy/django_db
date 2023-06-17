from django.urls import path
from . import views

urlpatterns = [
    path('good/', views.good, name='good'),
    path('client/', views.client, name='client'),
    path('order/', views.order, name='order'),
    path('good/<str:id>/delete/', views.delete_good, name = "delete_good"),
    path('client/<int:id>/delete/', views.delete_client, name = "delete_client"),
    path('order/<int:id>/delete/', views.delete_order, name = "delete_order"),
# 'forms/client/<int:data_id>/delete/'
#     forms/client/<str:data_id>/delete/
]