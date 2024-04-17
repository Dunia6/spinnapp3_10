from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login, logout, authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer ,ProfileSerialiser
from .models import Profile



class RegisterView(APIView):
    """ La vue de l'enregistrement """
    permission_classes = [AllowAny]  # Allow anyone to register

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    """ La vue de connexion """
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    """ La vue de déconnexion """
    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)


class ProfileView(APIView):
    """ La vue du profile """
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, pk=None):
        try:
            profile = Profile.objects.get(pk=pk)
            serializer = ProfileSerialiser(Profile)
            return Response(serializer.data)
        except Profile.DoesNotExist:
            return Response({'error': 'Profile introuvable !'}, status=404)
    
    def post(self, request):
        user = request.user
        serializer = ProfileSerialiser(Profile, data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        
    
    def put(self, request, pk, format=None):
        user = request.user
        
        try:
            profile = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Response({'error': 'Profile introuvable !'}, status=400)

        if profile.user != user:
            return Response({'error': 'Vous ne pouvez modifier que votre propre profil'}, status=403)
        
        serialiser = ProfileSerialiser(Profile, data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data)
        return Response(serialiser.errors, status=400)