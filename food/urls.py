from.import views
from django.urls import path

urlpatterns=[
    path('', views.index, name='index'),
    path('items/', views.items, name='items'),
    path('<int:itemid>/', views.detail, name='detail'),
    path('additems/', views.additems.as_view(), name='additems'),
    path('edititem/<itemid>/', views.edititem, name='edititem'),
    path('deleteitem/<itemid>/', views.deleteitem, name='deleteitem'),
]