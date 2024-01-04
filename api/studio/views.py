from rest_framework.viewsets import ModelViewSet
from studio.models import (
    Category, MainCategory, Project
)
from rest_framework.permissions import (IsAuthenticatedOrReadOnly)
from .serializers import MainCategorySerializer, CategorySerializer, ProjectSerializer

class MainCategoryViewset(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = MainCategory.objects.all()
    serializer_class = MainCategorySerializer
    

class CategoryViewset(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
class ProjectViewset(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer