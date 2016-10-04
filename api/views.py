#-*- coding: utf-8 -*-

from rest_framework import viewsets
from rest_framework.response import Response
from . import models
from . import serializers
from django.contrib.auth.models import User

class CommentViewSet(viewsets.ModelViewSet):
    """
    이 뷰셋은 `list`와 `create`, `retrieve`, `update`, 'destroy` 기능을 자동으로 지원합니다

    """
    queryset=models.Comment.objects.all()
    serializer_class=serializers.CommentSerializer
    
class UploadViewSet(viewsets.ModelViewSet):
    """
    이 뷰셋은 `list`와 `create`, `retrieve`, `update`, 'destroy` 기능을 자동으로 지원합니다

    """
    serializer_class=serializers.UploadSerializer
    
    def get_queryset(self):
        actor_id = self.request.GET.get('actor_id')
        if actor_id and actor_id != 'false' and actor_id != '1':
            return models.Upload.objects.filter(user_id=actor_id).order_by('-created_at')
        return models.Upload.objects.all().order_by('-created_at')
    
class LikeViewSet(viewsets.ModelViewSet):
    """
    이 뷰셋은 `list`와 `create`, `retrieve`, `update`, 'destroy` 기능을 자동으로 지원합니다

    """
    queryset=models.Like.objects.all()
    serializer_class=serializers.LikeSerializer

class FollowViewSet(viewsets.ModelViewSet):
    """
    이 뷰셋은 `list`와 `create`, `retrieve`, `update`, 'destroy` 기능을 자동으로 지원합니다

    """
    queryset=models.Follow.objects.all()
    serializer_class=serializers.FollowSerializer
    


class UserViewSet(viewsets.ReadOnlyModelViewSet):  
    """
    이 뷰셋은 `list`와 `detail` 기능을 자동으로 지원합니다
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


from actstream.models import user_stream, Action

class ActivityViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.ActionSerializer

    def get_queryset(self):
        
        #/api/activity/?following=1
        following = self.request.GET.get('following')
        if following and following != 'false' and following != '0':
            if following == 'myself':
                qs = user_stream(self.request.user, with_user_activity=True)
                return qs.filter(actor_object_id=self.request.user.id)
            else:  # Everyone else but me
                return user_stream(self.request.user)
        return Action.objects.all()

    filter_fields = (
        'actor_content_type', 'actor_content_type__model',
        'target_content_type', 'target_content_type__model',
    )