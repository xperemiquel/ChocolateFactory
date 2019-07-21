from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import OompaLoompa
from .serializers import OompaLoompaSerializer, OompaLoompaListSerializer


class OompaLoompaViewSet(ModelViewSet):

    queryset = OompaLoompa.objects.all() 
    permission_classes = [ AllowAny ] # not recommended in production
    serializer_class = OompaLoompaSerializer
    allowed_methods = ('GET', 'POST', 'PUT', 'PATCH') # just for info in the browsable api viewer
    http_method_names = ('get', 'post', 'put', 'patch')
    
    def list(self, request):
        queryset = OompaLoompa.objects.all().only('name', 'age', 'job')
        paginated_queryset = self.paginate_queryset(queryset) # pagination config in settings.py
        serializer = OompaLoompaListSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    @method_decorator(cache_page(60 * 60)) # cached 1 hour for all users
    def dispatch(self, *args, **kwargs):
        return super(OompaLoompaViewSet, self).dispatch(*args, **kwargs)