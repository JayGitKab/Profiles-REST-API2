# System/framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status                               # HTTP statues
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


# imports fro our application
from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloAPIView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses Http methods as functions (get, post, patch, put, delete)',
            'Is simillar to a traditional Django view',
            'Gives you the most control over the application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello', 'an_apiview': an_apiview})

    def post(self, request):
            """ Create a hello message with our name"""
            serializer = self.serializer_class(data=request.data)

            if serializer.is_valid():
                name = serializer.validated_data.get('name')
                message = f'Hello {name}'
                return Response({'message' : message})
            else:
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                    )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object """
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Retun a Hllow message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to uRLs using routers',
            'Provides more functionality with less code',
        ]

        return Response ({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'retrieve'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method':'update'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method':'partial_update'})

    def destroy(self, request, pk=None):
        """Handle removing and object"""
        return Response({'http_method':'destroy'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    # Add Token and password to allow user to only change themselves
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
    # to allow filtering by name and email
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email', )

class UserLoginApiView(ObtainAuthToken):
    """Handle creataing user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authenication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
