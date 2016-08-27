from django.contrib import admin
from .models import Comment,Follow,Search,Like,Upload,Hashtag

# Register your models here.
admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(Search)
admin.site.register(Like)
admin.site.register(Upload)
admin.site.register(Hashtag)
