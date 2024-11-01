from rest_framework import (
    permissions,
    generics,
)
from drf_spectacular.utils import extend_schema

from user.serializers import UserSerializer
from user.models import User

from django.shortcuts import render


@extend_schema(tags=['Me'])
class UserMeView(generics.RetrieveUpdateAPIView):
    """ View for authenticated user. """

    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """ Retrieve and return the authenticated user. """
        return self.request.user


def index(request):
    return render(request, 'index.html')
