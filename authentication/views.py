from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import RegisterMemberSerializer, RegisterLibrarianSerializer, LoginSerializer
from rest_framework import status
from rest_framework_simplejwt.views import TokenViewBase

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from swagger_responses import login_response_schema,register_response_schema
# Create your views here.


class RegisterMember(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(request_body=RegisterMemberSerializer, operation_description="Register a new member",
                         responses=register_response_schema)
    def post(self, request, *args, **kwargs):
        serializer = RegisterMemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"detail": "You have registered successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"detail": "Bad request", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )


class RegisterLibrarian(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(request_body=RegisterLibrarianSerializer, operation_description="Register a new librarian",
                         responses=register_response_schema)
    def post(self, request, *args, **kwargs):
        serializer = RegisterLibrarianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"detail": "Librarian registration successful", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"detail": "Bad request", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )


class Login(TokenViewBase):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    @swagger_auto_schema(request_body=LoginSerializer, operation_description="Login a user",
                         responses=login_response_schema)
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            {"status": 200, "detail": "Login successful", "data": serializer.validated_data}, status=status.HTTP_200_OK
        )
