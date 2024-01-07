from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

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
