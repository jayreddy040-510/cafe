from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from .models import User
# Create your views here.
users = User.objects.all()
@api_view(['GET'])
def getRoutes(request):
    return Response('Our Response')

@api_view(['GET'])
def getUsers(request):

    serializer = UserSerializer(users, many=True)
    print(serializer.data)
    return Response(serializer.data)

@api_view(['GET'])
def getUser(request, id):
    user = User.objects.get(id=id)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)