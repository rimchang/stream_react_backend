from datetime import datetime
from uuid import uuid4
from urllib2 import urlopen, HTTPError
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.files.base import ContentFile
from api.models import UserProfile


def get_profile_data(backend, user, response, *args, **kwargs):
    profile, new_user = UserProfile.objects.get_or_create(user=user)

    if backend.__class__.__name__ == 'FacebookOAuth2':   # changed from FacebookBackend, no effect

        if not user.email and response.get('email'):
            user.email = response.get('email')
            
        if not profile.name and response.get('name'):
            profile.name = response.get('name')
            
        #if not profile.age_range and response.get('age_range'):    
        if response.get('age_range'):
            age_range = response.get('age_range')
            try:
                profile.age_range_min = age_range["min"]
            except:
                pass
            try:
                profile.age_range_max = age_range["max"]
            except:
                pass

        #if not profile.gender and response.get('gender'):
        if response.get('gender'):
            profile.gender = response.get('gender')
            
        if not profile.link and response.get('link'):
            profile.link = response.get('link')   
            
        if not profile.locale and response.get('locale'):
            profile.locale = response.get('locale')
        profile.save()
        user.save()


def get_profile_avatar(backend, user, response, *args, **kwargs):
    url = None
    profile = user.userprofile
    if not profile.profile_photo:
        if backend.__class__.__name__ == 'FacebookOAuth2':
            url = "http://graph.facebook.com/%s/picture?type=large" % \
                  response.get('id')

        if url:
            try:
                avatar = urlopen(url)
                rstring = uuid4().get_hex()
                profile.profile_photo.save(slugify(rstring + '_p') + '.jpg',
                                           ContentFile(avatar.read()))
                profile.save()
            except HTTPError:
                pass
            
            
            