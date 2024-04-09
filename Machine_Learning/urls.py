from django.urls import path
from . import views

urlpatterns = [
    path('ml/', views.machine_learning, name= 'machine'),
    path('random/', views.random_forest, name= 'rf'),
    path('dt/', views.data_tree, name= 'dt'),
    path('kn/', views.kn, name= 'kn'),
]