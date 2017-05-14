from django.conf.urls import  url

from views import available_companies

urlpatterns = [
    url(r'^available-companies/$', available_companies, name='companies-list'),
]