from django.contrib.auth.models import User, Group  
from rest_framework import serializers
from . import models



class CommentSerializer(serializers.ModelSerializer):  
    id = serializers.ReadOnlyField()
    class Meta:
        model = models.Comment
        fields = ('id','user_id','upload_id','comment')


class UploadSerializer(serializers.ModelSerializer): 
    id = serializers.ReadOnlyField()
    comments = serializers.SlugRelatedField(many=True,read_only=True,slug_field='comment')
    
    class Meta:
        model = models.Upload
        fields = ('id','user_id','image_file','caption','location','latitude','longitude','comments')


class LikeSerializer(serializers.ModelSerializer):  
    id = serializers.ReadOnlyField()
    class Meta:
        model = models.Like
        fields = ('id','user_id','upload_id')

class FollowSerializer(serializers.ModelSerializer):  
    id = serializers.ReadOnlyField()
    class Meta:
        model = models.Follow
        fields = ('id','user_id','follower_id')

class UserSerializer(serializers.ModelSerializer):  
    id = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = ('id', 'username')


from actstream.models import Action

class GenericRelatedField(serializers.Field):
    
    def to_representation(self, value):
        if isinstance(value, models.Comment):
            return CommentSerializer(value).data
        if isinstance(value, models.Like):
            return LikeSerializer(value).data
        if isinstance(value, models.Upload):
            return UploadSerializer(value).data
        if isinstance(value, models.Follow):
            return FollowSerializer(value).data
        if isinstance(value, User):
            return UserSerializer(value).data
        # Not found - return string.
        return str(value)

class ActionSerializer(serializers.ModelSerializer):
    actor = GenericRelatedField(read_only=True)
    target = GenericRelatedField(read_only=True)
    action_object = GenericRelatedField(read_only=True)

    class Meta:
        model = Action