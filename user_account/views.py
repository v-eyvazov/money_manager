from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from user_account.serializers import RegistrationSerializer
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


@api_view(['POST'])
@permission_classes([AllowAny])
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data['response'] = "successfully registered a new user."
        data['email'] = account.email
        data['username'] = account.username
    else:
        data = serializer.errors
    return Response(data)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """
    POST API for login
    """
    username = request.data['username']
    password = request.data['password']
    if username is None:
        return JsonResponse({
            "errors": {
                "detail": "Please enter username"
            }
        }, status=400)
    elif password is None:
        return JsonResponse({
            "errors": {
                "detail": "Please enter password"
            }
        }, status=400)

    # authentication user
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"success": "User has been logged in"})
    return JsonResponse(
        {"errors": "Invalid credentials"},
        status=400,
    )


@api_view(['GET'])
def logout_view(request):
    logout(request)
    return Response(status=status.HTTP_200_OK)
