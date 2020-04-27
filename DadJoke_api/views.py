from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status                               # HTTP statues
from rest_framework.settings import api_settings# Create your views here.
from rest_framework import viewsets


# imports fro our application
from DadJoke_api import serializers
from DadJoke_api import models

class DadJokeAPIView(APIView):
    """Test API View"""
    serializer_class = serializers.DadJokeSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses Http methods as functions (get, post, patch, put, delete)',
            'Is simillar to a traditional Django view',
            'Gives you the most control over the application logic',
            'Is mapped manually to URLs',
            'Jokes',
        ]

        return Response({'message':'Jokes', 'an_apiview': an_apiview})

    def post(self, request):
            """ Create a hello message with our name"""
            serializer = self.serializer_class(data=request.data)

            if serializer.is_valid():
                jokeQ = serializer.validated_data.get('joke_question')
                jokeA = serializer.validated_data.get('joke_answer')
                message = f'{jokeQ+jokeA}'
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


class DadJokeViewSet(viewsets.ViewSet):
    """DadJoke ViewSet"""
    serializer_class = serializers.DadJokeSerializer

    def list(self, request):
        """Returns a list of ViewSet features"""
        an_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to uRLs using routers',
            'Provides more functionality with less code',
            'Jokes',
        ]

        return Response({'message':'Jokes', 'an_viewset': an_viewset})

    def create(self, request):
            """ Create a DadJoke message"""
            serializer = self.serializer_class(data=request.data)

            if serializer.is_valid():
                jokeQ = serializer.validated_data.get('joke_question')
                jokeA = serializer.validated_data.get('joke_answer')
                message = f'{jokeQ+jokeA}'
                return Response({'message' : message})
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

class DadJokeFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    serializer_class = serializers.DadJokeFeedItemSerializer
    queryset = models.DadJokeFeedItem.objects.all()
