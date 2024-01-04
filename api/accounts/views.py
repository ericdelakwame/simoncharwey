from rest_framework.viewsets import ModelViewSet
from accounts.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import UserSerializer


class UserViewset(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = User.objects.order_by('last_name').filter(location__isnull=False)
    serializer_class = UserSerializer