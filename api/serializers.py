from django.contrib.auth.models import User, Group  
from rest_framework import serializers
from . import models

class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BaseModel
        fields=('created_at','modified_at')

class CommentSerializer(serializers.ModelSerializer):  
    id = serializers.ReadOnlyField()
    class Meta(BaseModelSerializer.Meta):
        model = models.Comment
        fields = ('id','user_id','upload_id','comment')

class LikeSerializer(serializers.ModelSerializer):  
    id = serializers.ReadOnlyField()
    class Meta(BaseModelSerializer.Meta):
        model = models.Like
        fields = ('id','user_id','upload_id')

class FollowSerializer(serializers.ModelSerializer):  
    id = serializers.ReadOnlyField()
    class Meta(BaseModelSerializer.Meta):
        model = models.Follow
        fields = ('id','user_id','follower_id')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('user','name','age_range_min','age_range_max','gender','locale','link','profile_photo')

class UserSerializer(serializers.ModelSerializer):  
    id = serializers.ReadOnlyField()
    
    userprofile = UserProfileSerializer()
    
    class Meta:
        model = User
        fields = ('id', 'username','email','first_name','last_name','userprofile')
"""
    def create(self, validated_data):
        profile_data = validated_data.pop('userprofile')
        user = User.objects.create(**validated_data)
        models.UserProfile.objects.create(user=user, **profile_data)
        return User
"""


class UploadSerializer(serializers.ModelSerializer): 
    id = serializers.ReadOnlyField()
    #image_url = serializers.SerializerMethodField('get_image_url')
    comments = CommentSerializer(many=True,read_only=True)
    
    user_id = UserSerializer(read_only=True)
    
    class Meta(BaseModelSerializer.Meta):
        model = models.Upload
        fields = ('id','user_id','image_file','caption','location','latitude','longitude','comments','created_at','modified_at')
        
class UploadCreateSerializer(serializers.ModelSerializer): 
    id = serializers.ReadOnlyField()
    #image_url = serializers.SerializerMethodField('get_image_url')
    comments = CommentSerializer(many=True,read_only=True)

    class Meta(BaseModelSerializer.Meta):
        model = models.Upload
        fields = ('id','user_id','image_file','caption','location','latitude','longitude','comments','created_at','modified_at')




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

    class Meta(BaseModelSerializer.Meta):
        model = Action
        fields = ('actor','verb','target','action_object')