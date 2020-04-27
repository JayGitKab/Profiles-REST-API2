from django.urls import path, include

from rest_framework.routers import DefaultRouter

from DadJoke_api import views

router = DefaultRouter()
router.register('DadJoke-viewset', views.DadJokeViewSet, base_name='DadJoke-viewset')
router.register('feed', views.DadJokeFeedViewSet)

urlpatterns = [
    path('DadJokes/', views.DadJokeAPIView.as_view(), ),
    path('', include(router.urls))

]
