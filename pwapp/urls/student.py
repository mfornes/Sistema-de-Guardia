from django.urls import path

from pwapp.views import StudentCreateView, StudentDeleteView, StudentDetailView, StudentListView, StudentUpdateView

urlpatterns = [
    path('student', StudentListView.as_view(), name='student-list'),
    path('student/create', StudentCreateView.as_view(), name='student-create'),
    path('student/<int:pk>', StudentDetailView.as_view(), name='student-detail'),
    path('student/<int:pk>/delete', StudentDeleteView.as_view(), name='student-delete'),
    path('student/<int:pk>/update', StudentUpdateView.as_view(), name='student-update'),
]