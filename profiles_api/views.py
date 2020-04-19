from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses Http methods as functions (get, post, patch, put, delete)',
            'Is simillar to a traditional Django view',
            'Gives you the most control over the application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello', 'an_apiview': an_apiview})
