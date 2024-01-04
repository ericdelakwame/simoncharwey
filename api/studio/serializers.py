from studio.models import (
    Project, Category, MainCategory, Project3D
)
from rest_framework.serializers import ModelSerializer, StringRelatedField

class Project3DSerializer(ModelSerializer):
    
    class Meta:
        model = Project3D
        fields = '__all__'
        

class ProjectSerializer(ModelSerializer):
    three_d_files = Project3DSerializer(many=True)
    class Meta:
        model = Project
        fields = '__all__'
        

class CategorySerializer(ModelSerializer):
    main_category = StringRelatedField()
    projects = ProjectSerializer(many=True)
    
    class Meta:
        model = Category
        fields = '__all__'
        
        

class MainCategorySerializer(ModelSerializer):
    categories = CategorySerializer(many=True)    
    class Meta:
        model = MainCategory
        fields = '__all__'        
