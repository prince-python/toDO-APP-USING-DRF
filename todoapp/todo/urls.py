from django.urls import path
from .import views
urlpatterns = [
    path('',views.Homeview),
    path('get/<int:pk',views.DetailView),
    path('create',views.CreateView),
    path('update/<int:pk>',views.CreateView),
    path('delete/<int:pk>',views.DeleteView)
]