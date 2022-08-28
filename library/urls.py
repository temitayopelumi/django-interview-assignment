from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from library import views

urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>/', views.BookDetail.as_view()),
    path('member/', views.UserList.as_view()),
    path('member/<int:pk>', views.UserDetail.as_view()),
    path('user/return-book/<int:pk>/', views.ReturnBook.as_view()),
    path('user/borrow-book/<int:pk>/', views.BorrowBook.as_view()),
    path('user/delete-account/', views.DeleteAccount.as_view()),
    
]
