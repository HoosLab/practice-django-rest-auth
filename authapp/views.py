from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from django.contrib.auth.models import User, Group
from rest_auth.registration.views import SocialLoginView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from authapp.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
