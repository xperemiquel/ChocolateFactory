from rest_framework import routers
from .views import OompaLoompaViewSet 

class OptionalTrailingSlashRouter(routers.DefaultRouter):

    def __init__(self, *args, **kwargs): 
        super(routers.DefaultRouter, self).__init__(*args, **kwargs) 
        self.trailing_slash = '/?'

router = OptionalTrailingSlashRouter()

router.register('v1/oompaloompas', OompaLoompaViewSet, 'oompaloompas') # url /oompaloompas with or without trailing slash

urlpatterns = router.urls

"""
OptionalTrailingSlashRouter endpoints:

ACTION    METHOD      URL

List      GET         api/v1/oompaloompas
Add       POST        api/v1/oompaloompas
Retrieve  GET         api/v1/oompaloompas/{id}
Edit      PUT,PATCH   api/v1/oompaloompas/{id}

*Works either with or without trailing slash
*All endpoints and methods tested with Postman

"""