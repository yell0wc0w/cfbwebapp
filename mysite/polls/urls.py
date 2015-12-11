from django.conf.urls import url
from . import views

app_name = 'polls'

urlpatterns = [
    # ex: /cfbwebapp/
    url(r'^$', views.AthleteView, name='index'),
    # ex: /cfbwebapp/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

]