from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from library import views

urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>/', views.BookDetail.as_view()),
    path('member/', views.UserList.as_view()),
    path('member/<int:pk>', views.UserDetail.as_view())
]
