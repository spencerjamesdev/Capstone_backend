from copy import error
from django.contrib.auth.models import User
from django.http import response
from django.http.response import Http404
from .serializers import RegistrationSerializer
from rest_framework import generics, serializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from django.contrib.auth.models import User

@api_view(['GET'])
@permission_classes([AllowAny])

# Gets all reminders from every user, probably wont be utalized
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_user_by_user_id(request, user_id):
    user = User.objects.get(pk = user_id)
    print(user_id)
    try:
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except (error):
        print(error)
        return Response(error)
  



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

