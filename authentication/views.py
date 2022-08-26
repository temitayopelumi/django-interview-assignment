from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import RegisterMemberSerializer, RegisterLibrarianSerializer
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi



# Create your views here.

response_schema_dict = {
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

class RegisterMember(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(request_body=RegisterMemberSerializer, operation_description="Register a new member", responses=response_schema_dict)
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

    @swagger_auto_schema(request_body=RegisterLibrarianSerializer, operation_description="Register a new librarian", responses=response_schema_dict)
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