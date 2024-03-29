from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from profiles_api import serializers, models, permissions
from rest_framework.authentication import TokenAuthentication


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    # APIView allows us to define application logic for our endpoint
    # URL: http://
    # HTTP methods: GET, POST, PATCH, PUT, DELETE
    # GET: retrieve a list or object
    # POST: create an object
    # PATCH: partially update an object
    # PUT: completely update an object
    # DELETE: delete an object

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            "Uses HTTP methods as functions (get, post, patch, put, delete)",
            "Is similar to a traditional Django View",
            "Gives you the most control over your application logic",
            "Is mapped manually to URLs",
        ]

        return Response({"message": "Hello!", "an_apiview": an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}!"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # pk is the primary key of the object we want to update
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({"method": "DELETE"})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            "Uses actions (list, create, retrieve, update, partial_update)",
            "Automatically maps to URLs using Routers",
            "Provides more functionality with less code",
        ]

        return Response({"message": "Hello!", "a_viewset": a_viewset})

    def create(self, request):
        """Create a new hello message"""

        # We use the serializer to validate the data
        serializer = self.serializer_class(data=request.data)

        # If the data is valid, we return a response with the message
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}!"
            return Response({"message": message})
        # If the data is not valid, we return a response with the errors
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # pk is the primary key of the object we want to retrieve
    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({"http_method": "GET"})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({"http_method": "PUT"})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({"http_method": "PATCH"})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({"http_method": "DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    serializer_class = serializers.UserProfilesSerializer
    queryset = models.UserProfile.objects.all()

    # We add the authentication_classes and permission_classes attributes to the viewset class to specify the authentication and permission classes that we want to use for the viewset

    authentication_classes = (
        TokenAuthentication,
    )  # the comma is needed to make it a tuple

    permission_classes = (permissions.UpdateOwnProfile,)

    # We add the filter_backends attribute to the viewset class to specify the filter backends that we want to use for the viewset

    filter_backends = (filters.SearchFilter,)
    # We add the search_fields attribute to the viewset class to specify the fields that we want to search on
    search_fields = (
        "name",
        "email",
    )
