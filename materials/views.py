# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Materials
from serializers import MaterialsSerializer
from rest_framework import routers, serializers, viewsets



class MaterialsViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = MaterialsSerializer
    queryset = Materials.objects.all()