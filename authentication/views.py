from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import RegisterMemberSerializer, RegisterLibrarianSerializer, LoginSerializer
from rest_framework import status
from rest_framework_simplejwt.views import TokenViewBase

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.

register_response_schema = {
    "201": openapi.Response(
        description="custom 201 description",
        examples={
            "application/json": {
                "message": "success",
                "data": {
                    "id": 3,
                    "username": "string"
                }
            }
        }
    ),
    "400": openapi.Response(
        description="custom 400 description",
        examples={
            "application/json": {
                "message": "failed",
                "data": {
                    "username": [
                        "This field is required."
                    ],
                    "password1": [
                        "This field is required."
                    ],
                    "password2": [
                        "This field is required."
                    ]
                }
            }

        }
    ),
}

login_response_schema = {
    "200": openapi.Response(
        description="custom 200 description",
        examples={
            "application/json": {
                "message": "success",
                "data": {
                    "refresh": ".4SMSPOVYXgX3vOV1R0qHtMPgASYtqZOepeoFR1eh4TI",
                    "access": "k6uEHiwl6H0okwDG0UlMWAno4dIo_FNaL3ToHCVxHkU",
                    "lifetime": 3600,
                    "role": "Member"
                }
            }
        }
    ),
    "401": openapi.Response(
        description="custom 400 description",
        examples={
            "application/json": {
                "detail": "No active account found with the given credentials"
            }

        }
    ),
}


class RegisterMember(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(request_body=RegisterMemberSerializer, operation_description="Register a new member",
                         responses=register_response_schema)
    def post(self, request, *args, **kwargs):
        serializer = RegisterMemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"message": "failed", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
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
                {"message": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"message": "failed", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
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
            {"status": 200, "message": "success", "data": serializer.validated_data}, status=status.HTTP_200_OK
        )
