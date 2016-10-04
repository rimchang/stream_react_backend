from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
admin.site.register(models.Comment)
admin.site.register(models.Follow)
admin.site.register(models.Search)
admin.site.register(models.Like)
admin.site.register(models.Upload)
admin.site.register(models.Hashtag)
#admin.site.register(models.UserProfile)

# for onotoone field admin
class UserProfileInline(admin.StackedInline):
    model = models.UserProfile
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = (UserProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)