from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('Hello-viewset', views.HelloViewSet, base_name='Hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('Hello-view/', views.HelloAPIView.as_view()),
    path('login/', views.UserLoginApiView.as_view(), ),
    path('', include(router.urls))
]
