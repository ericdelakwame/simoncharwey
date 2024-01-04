from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.studio.views import (
    MainCategoryViewset, CategoryViewset, ProjectViewset
)
from api.accounts.views import (
    UserViewset
)

from api.citation.views import CitationViewset

router = DefaultRouter()

router.register('main/categories', MainCategoryViewset, basename='main_categories')
router.register('categories', CategoryViewset, basename='categories'),
router.register('projects', ProjectViewset, basename='projects'),
router.register('users', UserViewset, basename='users'),
router.register('citations', CitationViewset, basename='citations'),

urlpatterns = [
    path('', include(router.urls)),
]
