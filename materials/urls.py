from django.conf.urls import  url

from .views import  MaterialsViewSet

urlpatterns = [
    url(r'^available-materials/$', MaterialsViewSet.as_view({'get':'list'}), name='materials-list'),
]