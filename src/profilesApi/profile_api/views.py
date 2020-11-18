from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import  serializers 
from rest_framework import status

# Create your views here.
class HelloAPIView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiView = [
            'Uses HTTP methods as functions (get, put, post, patch, del)',
            'It is similar to a traditional Django view',
            'Gives you most control over your logic',
            'Is manually mapped to URLs'
        ]

        return Response({'message':'Hello!','an_apiView':an_apiView})
    
    def post(self, request):
        """Creates a hello message with our name"""
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:

            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)