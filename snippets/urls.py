from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)


# API endpoints
urlpatterns = [
    path('', include(router.urls)),
]
# The DefaultRouter class we're using also automatically creates the API root view for us, so we can now delete the api_root method from our views module.