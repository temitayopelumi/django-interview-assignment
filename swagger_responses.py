from email.mime import application
from drf_yasg import openapi


login_response_schema = {
    "401": openapi.Response(
        description ="wrong username or password",
        examples= {
            "application/json": {
                "detail": "No active account found with the given credentials"
            }
        }
    ),
    "200": openapi.Response(
        description="successful login",
        examples={
            "application/json": {
                "detail": "success",
                "data": {
                    "refresh": "jwt_token",
                    "access": "jwt_token",
                    "lifetime": "time",
                    "role": "string"
                }
            },
            "application/json": {
                "detail": "success",
                "data": {
                    "refresh": ".4SMSPOVYXgX3vOV1R0qHtMPgASYtqZOepeoFR1eh4TI",
                    "access": "k6uEHiwl6H0okwDG0UlMWAno4dIo_FNaL3ToHCVxHkU",
                    "lifetime": "3600",
                    "role": "Librarian"
                }
            }
        },
    )
}

register_response_schema = {
    "201": openapi.Response(
        description="custom 201 description",
        examples={
            "application/json": {
                "detail": "success",
                "data": {
                    "id": "int",
                    "username": "string"
                }
            }
        }
    ),
    "400": openapi.Response(
        description="custom 400 description",
        examples={
            "application/json": {
                "detail": "failed",
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


get_books_response_schema = {
    "401": openapi.Response(
        description="unauthorized",
        examples= {
            "application/json": {
                "detail": "Authentication credentials were not provided."
            }
        }
    ),
    "200": openapi.Response(
        description= "200",
        examples={
            "application/json":{
                "detail": "Books retrieved successfully",
                "data": [
                    {
                    "title": "string",
                    "author": "string"
                    }
                ]
            }
        }
    )
}


create_book_response_schema = {
    "401": openapi.Response(
        description="unauthorized",
        examples= {
            "application/json": {
                "detail": "Authentication credentials were not provided."
            }
        }
    ),
    "403": openapi.Response(
        description="forbidden",
        examples= {
            "application/json": {
                "detail": "You do not have permission to perform this action."
            }
        }
    ),
    "201": openapi.Response(
        description="CREATED",
        examples={
            "application/json": {
                "detail": "Book created successfully",
                "data": {
                    "title": "string",
                    "author": "string"
                }
            }
        }
    )

}

get_a_book_response_schema = {
    "401": openapi.Response(
        description="unauthorized",
        examples= {
            "application/json": {
                "detail": "Authentication credentials were not provided."
            }
        }
    ),
    "200": openapi.Response(
        description= "200",
        examples={
            "application/json": {
                "detail": "Book retrieved successfully",
                    "data": {
                        "title": "string",
                        "author": "string"
                    }
            }
        }
    ),
    "404": openapi.Response(
        description="Not found",
        examples= {
            "application/json": { 
                "detail": "Not found."
            }
        }
    )

}

update_a_book_response_schema = {
    "401": openapi.Response(
        description="unauthorized",
        examples= {
            "application/json": {
                "detail": "Authentication credentials were not provided."
            }
        }
    ),
    "403": openapi.Response(
        description="forbidden",
        examples= {
            "application/json": {
                "detail": "You do not have permission to perform this action."
            }
        }
    ),
    "404": openapi.Response(
        description="Not found",
        examples= {
            "application/json": { 
                "detail": "Not found."
            }
        }
    ),
     "200": openapi.Response(
        description="OK",
        examples={
            "application/json": {
                "detail": "Book updated successfully",
                "data": {
                    "title": "string",
                    "author": "string"
                }
            }
        }
    )
}

delete_a_book_response_schema = {
    "401": openapi.Response(
        description="unauthorized",
        examples= {
            "application/json": {
                "detail": "Authentication credentials were not provided."
            }
        }
    ),
    "403": openapi.Response(
        description="forbidden",
        examples= {
            "application/json": {
                "detail": "You do not have permission to perform this action."
            }
        }
    ),
    "404": openapi.Response(
        description="Not found",
        examples= {
            "application/json": { 
                "detail": "Not found."
            }
        }
    ),
    "200": openapi.Response(
        description="Not found",
        examples= {
            "application/json": { 
                "detail": "Book deleted successfully."
            }
        }
    )
}

get_members_response_schema = {
    "401": openapi.Response(
        description="unauthorized",
        examples= {
            "application/json": {
                "detail": "Authentication credentials were not provided."
            }
        }
    ),
    "403": openapi.Response(
        description="forbidden",
        examples= {
            "application/json": {
                "detail": "You do not have permission to perform this action."
            }
        }
    ),
    "200": openapi.Response(
        description="OK",
        examples={
            "application/json": {
                "detail": "User retrieved successfully",
                "data": [
                    {
                        "username": "string"
                    },
                    {
                        "username": "string"
                    }
                ]
            }
        }
    )
}


create_member_response_schema = {
    "401": openapi.Response(
        description="unauthorized",
        examples= {
            "application/json": {
                "detail": "Authentication credentials were not provided."
            }
        }
    ),
    "403": openapi.Response(
        description="forbidden",
        examples= {
            "application/json": {
                "detail": "You do not have permission to perform this action."
            }
        }
    ),
    "200": openapi.Response(
        description="OK",
        examples={
            "application/json": {
                "detail": "User created successfully",
                "data": {
                    "username": "string"
                    }
            }
        }
    )
}

get_a_member_response_schema = {
    "401": openapi.Response(
        description="unauthorized",
        examples= {
            "application/json": {
                "detail": "Authentication credentials were not provided."
            }
        }
    ),
    "403": openapi.Response(
        description="forbidden",
        examples= {
            "application/json": {
                "detail": "You do not have permission to perform this action."
            }
        }
    ),
    "200": openapi.Response(
        description="OK",
        examples={
            "application/json": {
                "detail": "User Retrieved successfully",
                "data": {
                    "username": "string"
                    }
            }
        }
    ),
     "404": openapi.Response(
        description="Not found",
        examples= {
            "application/json": { 
                "detail": "Not found."
            }
        }
    )
}

update_a_member_response_schema = {
    "401": openapi.Response(
        description="unauthorized",
        examples= {
            "application/json": {
                "detail": "Authentication credentials were not provided."
            }
        }
    ),
    "403": openapi.Response(
        description="forbidden",
        examples= {
            "application/json": {
                "detail": "You do not have permission to perform this action."
            }
        }
    ),
     "404": openapi.Response(
        description="Not found",
        examples= {
            "application/json": { 
                "detail": "Not found."
            }
        }
    ),
    "200": openapi.Response(
        description="OK",
        examples={
            "application/json":{         
                "detail": "User updated successfully",
                "data": {
                    "username": "string"
                }
            }
        }
    )
}

delete_a_member_response_schema = {
    "401": openapi.Response(
        description="unauthorized",
        examples= {
            "application/json": {
                "detail": "Authentication credentials were not provided."
            }
        }
    ),
    "403": openapi.Response(
        description="forbidden",
        examples= {
            "application/json": {
                "detail": "You do not have permission to perform this action."
            }
        }
    ),
     "404": openapi.Response(
        description="Not found",
        examples= {
            "application/json": { 
                "detail": "Not found."
            }
        }
    ),
    "200": openapi.Response(
        description="OK",
        examples={
            "application/json":{                     
                "detail": "User deleted successfully"
            }
        }
    )
}

return_book_response_schema = {
    "401": openapi.Response(
        description="unauthorized",
        examples= {
            "application/json": {
                "detail": "Authentication credentials were not provided."
            }
        }
    ),
    "200": openapi.Response(
        description="OK",
        examples={
            "application/json":{                     
                "detail": "Book returned"
            }
        }
    ),
     "404": openapi.Response(
        description="Not found",
        examples= {
            "application/json": { 
                "detail": "Not found."
            }
        }
    ),
}

borrow_book_response_schema = {
     "401": openapi.Response(
        description="unauthorized",
        examples= {
            "application/json": {
                "detail": "Authentication credentials were not provided."
            }
        }
    ),
    "200": openapi.Response(
        description="OK",
        examples={
            "application/json":{                     
               "detail": "You have been borrowed the book"
            }
        }
    ),
     "404": openapi.Response(
        description="Not found",
        examples= {
            "application/json": { 
                "detail": "Not found."
            }
        }
    ),
}

delete_account_response_schema={
    "401": openapi.Response(
        description="unauthorized",
        examples= {
            "application/json": {
                "detail": "Authentication credentials were not provided."
            }
        }
    ),
    "200": openapi.Response(
        description="OK",
        examples={
            "application/json":{                     
                "detail": "Account deleted. You will no longer have access to this service"

            }
        }
    ),
}



