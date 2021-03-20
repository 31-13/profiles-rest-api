from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers

class HelloApiView(APIView):
    """test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format = None):
        """ Returns a list of APIViews features"""
        an_apiview = [
            "Uses HTTP methods as function (get, post, patch, put, delete)",
            "Is similar to a traditional Django View",
            "Gives you the most control over your application object",
            "Is mapped mannualy to URLs",
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with out name"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"hello {name}!"
            return Response({'message': message})
        return Response(
        serializer.errors,
        status = status.HTTP_400_BAD_REQUEST
        )

    def put(self, request, pk = None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk = None):
        """handle a partial update of an object"""
        return Response({'method' : 'PATCH'})

    def delete(self, request, pk = None):
        """Delete an object"""
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test api view set"""
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Return a Hello message"""

        a_viewset = [
         "uses actions(list, create, retrieve, udpate, partial_update)",
         "automatically maps to URLs using Routers",
         "Provides more functionality with less code"
        ]
        return Response({"message" : "hello!", "a_viewset": a_viewset})

    def create(self, request):
        """Create a new hellow message"""
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"hello {name}!"
            return Response({'message' : message})
        return Response(serializer.errors,
                    status = status.HTTP_400_BAD_REQUEST
                    )

    def retrieve(self, request, pk = None):
        """Handle object by id"""

        return Response({"http_method" : "GET"})

    def update(self, request, pk = None):
        """Hanlde updating object"""
        return Response({"http_method" : "PUT"})

    def partial_update(self, request, pk = None):
        """Hanlde update part of an object"""
        return Response({'http_method' : 'PATCH'})

    def destroy(self, request, pk = None):
        """Remove an object"""
        return Response({'http_method' : 'DELETE'})
