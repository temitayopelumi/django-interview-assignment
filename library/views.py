from authentication.models import User
from django.core.exceptions import PermissionDenied
from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from swagger_responses import (create_book_response_schema,
                               create_member_response_schema,
                               delete_a_book_response_schema,
                               delete_a_member_response_schema,
                               get_a_book_response_schema,
                               get_a_member_response_schema,
                               get_books_response_schema,
                               get_members_response_schema,
                               update_a_book_response_schema,
                               update_a_member_response_schema)

from .models import Book
from .serializers import BookSerializer, UserSerializer


# Create your views here.
def check_permission(user):
    if user.role == 'Librarian':
        pass
    else:
        raise PermissionDenied()


class BookList(APIView):
    """
    List all books, or create a new book.
    """

    @swagger_auto_schema(operation_description="Get the list of books", responses=get_books_response_schema)
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({"detail": "Books retrieved successfully", "data": serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=BookSerializer, operation_description="Add a new book to the library", responses=create_book_response_schema)
    def post(self, request):
        check_permission(request.user)
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Book created successfully", "data": serializer.data},
                            status=status.HTTP_200_OK)
        return Response({"detail": "Bad request", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):
    """
    Retrieve, update or delete a book instance.
    """

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    @swagger_auto_schema(operation_description="Get a book", responses=get_a_book_response_schema)
    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response({"detail": "Book retrieved successfully", "data": serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=BookSerializer, operation_description="update book", responses=update_a_book_response_schema)
    def patch(self, request, pk):
        check_permission(request.user)
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data, context={"request": request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Book updated successfully", "data": serializer.data},
                            status=status.HTTP_200_OK)
        return Response({"detail": "Bad request", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        check_permission(request.user)
        book = self.get_object(pk)
        book.delete()
        return Response({"detail": "Book deleted successfully"}, status=status.HTTP_200_OK)


class UserList(APIView):
    """
    List all books, or create a new book.
    """

    @swagger_auto_schema(operation_description="Get the list of members", responses=get_members_response_schema)
    def get(self, request):
        check_permission(request.user)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"detail": "User retrieved successfully", "data": serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=UserSerializer, operation_description="Add a new member to the library", responses=create_member_response_schema)
    def post(self, request):
        check_permission(request.user)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "User created successfully", "data": serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response({"detail": "Bad request", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    Retrieve, update or delete a book instance.
    """

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    @swagger_auto_schema(operation_description="Get a member", responses=get_a_member_response_schema)
    def get(self, request, pk):
        check_permission(request.user)
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response({"detail": "User retrieved successfully", "data": serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=UserSerializer, operation_description="update member", responses=update_a_member_response_schema)
    def patch(self, request, pk):
        check_permission(request.user)
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data, context={"request": request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "User updated successfully", "data": serializer.data},
                            status=status.HTTP_200_OK)
        return Response({"detail": "Bad request", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        check_permission(request.user)
        user = self.get_object(pk)
        user.delete()
        return Response({"detail": "User deleted successfully"}, status=status.HTTP_200_OK)


class ReturnBook(APIView):

    def patch(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404
        if book.status == "AVAILABLE":
            return Response({"detail": "Book is availiable"}, status=status.HTTP_200_OK)
        book.status = "AVAILABLE"
        book.save()
        return Response({"detail": "Book returned"}, status=status.HTTP_200_OK)


class BorrowBook(APIView):

    def patch(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404
        if book.status == "BORROWED":
            return Response({"detail": "Book has been borrowed"}, status=status.HTTP_200_OK)
        book.status = "BORROWED"
        book.save()
        return Response({"detail": "You have been borrowed the book"}, status=status.HTTP_200_OK)


class DeleteAccount(APIView):
    def post(self, request):
        user = request.user
        user.delete()
        return Response({"detail": "Account deleted. You will no longer have access to this service"},
                        status=status.HTTP_200_OK)
