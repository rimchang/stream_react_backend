from datetime import datetime
from uuid import uuid4
from urllib2 import urlopen, HTTPError
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.files.base import ContentFile
from django.contrib.auth.models.User import UserProfile


def get_profile_data(backend, details, response, social_user,
                     uid, user, *args, **kwargs):
    profile, new_user = UserProfile.objects.get_or_create(user=user)

    if backend.__class__.__name__ == 'FacebookOAuth2':   # changed from FacebookBackend, no effect

        if not user.email and response.get('email'):
            user.email = response.get('email')

        if not profile.gender and response.get('gender'):
            profile.gender = response.get('gender')

        if not profile.birthday and response.get('birthday'):
            datestring = response.get('birthday')
            date_format = "%m/%d/%Y"
            profile.birthday = datetime.strptime(datestring, date_format)

        profile.save()
        user.save()


def get_profile_avatar(backend, details, response, social_user,
                       uid, user, *args, **kwargs):
    url = None
    profile = user.get_profile()
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