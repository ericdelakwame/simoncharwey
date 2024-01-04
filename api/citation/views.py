from rest_framework.viewsets import ModelViewSet
from citation.models import Citation
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import CitationSerializer



class CitationViewset(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = Citation.objects.order_by('-created')
    serializer_class = CitationSerializer