from datetime import datetime
from uuid import uuid4
from urllib2 import urlopen, HTTPError
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.files.base import ContentFile
from models import UserProfile


def get_profile_data(backend, details, response, social_user,
                     uid, user, *args, **kwargs):
    profile, new_user = UserProfile.objects.get_or_create(user=user)

    if backend.__class__.__name__ == 'FacebookOAuth2':   # changed from FacebookBackend, no effect

        if not profile.email and response.get('email'):
            profile.email = response.get('email')
            
        if not profile.name and response.get('name'):
            profile.name = response.get('name')
            
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
    profile = UserProfile()
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
            
# User details pipeline
def user_details(strategy, details, response, user=None, *args, **kwargs):
    """Update user details using data from provider."""
    if user:
        # ...
        # Just created the user?
        if kwargs['is_new']:
            attrs = {'user': user}
            # I am using also Twitter backend, so I am checking if It's FB
            # or Twitter. Might be a better way of doing this
            if strategy.backend.__class__.__name__ == 'FacebookOAuth2':
                # We should check values before this, but for the example
                # is fine
                fb_data = {
                    'city': response['location']['name'],
                    'gender': response['gender'],
                    'locale': response['locale'],
                }
                attrs = dict(attrs.items() + fb_data.items())
            UserProfile.objects.create(
                **attrs
            )