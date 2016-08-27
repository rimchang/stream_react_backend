# myapp/apps.py
from django.apps import AppConfig, apps
from drf_react import settings

class MyAppConfig(AppConfig):
    name = 'api'

    def ready(self):
        from actstream import registry
        registry.register(apps.get_model('api.Comment'))
        registry.register(apps.get_model('api.Follow'))
        registry.register(apps.get_model('api.Like'))
        registry.register(apps.get_model('api.Search'))
        registry.register(apps.get_model('api.Upload'))
        registry.register(apps.get_model('auth.user'))



