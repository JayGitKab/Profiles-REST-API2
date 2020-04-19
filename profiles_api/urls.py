from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('Hello-viewset', views.HelloViewSet, base_name='Hello-viewset')
 
urlpatterns = [
    path('Hello-view/', views.HelloAPIView.as_view()),
    path('', include(router.urls))
]
