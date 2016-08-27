from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()  
router.register(r'comments', views.CommentViewSet)
router.register(r'uploads', views.UploadViewSet)
router.register(r'likes', views.LikeViewSet)
router.register(r'follows', views.FollowViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'activity', views.ActivityViewSet, base_name='activity')

urlpatterns = [
    url(r'^', include(router.urls)),
    
]
