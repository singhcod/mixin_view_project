from django.urls import path

from mixin_app import views

urlpatterns = [
    path('employee/',views.EmployeeListView.as_view()),
    path('employee/<int:pk>/',views.EmployeeDetailView.as_view()),
]