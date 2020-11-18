from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import  serializers 
from rest_framework import status
from rest_framework import viewsets
from . import models
from . import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken


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


    def put(self, request, pk=None):
        """Handels updating an object with pk=primary key"""

        return Response({'method':'put'})


    def patch(self, request, pk=None):
        """Handels patching an object with pk=primary key"""

        return Response({'method':'patch'})

    def delete(self, request, pk=None):
        """Handels deleting an object with pk=primary key"""

        return Response({'method':'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test api viewset"""

    serializer_class = serializers.HelloSerializer

    def list(self, reque):
        """This is going to return a hello message"""
        a_viewse = [
            'Uses acions (lis, cae, retrieve, updte, parial_upde)',
            'Automaially mapsthurlssinroutrs',
            'Proves morecnaliwithlssoe'
        ]

        return Response({'message':'Hello','a_viewset':a_viewse})
    
    def create(self, request):
        """Create anew hello message"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handels getting an object by its ID"""

        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Handels updating an object by its ID"""

        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handels partial updating an object by its ID"""

        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Handels removing an object by its ID"""

        return Response({'http_method':'Delete'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permissions_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('firstName','email',)

class LoginViewSet(viewsets.ViewSet):
    """Check email and password and return an auth token"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the obtainAuthtoken apiview to Validate and create a token"""

        return ObtainAuthToken().post(request)
