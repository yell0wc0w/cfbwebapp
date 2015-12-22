from django.conf.urls import url
from . import views

app_name = 'polls'

urlpatterns = [
    # ex: /cfbwebapp/
    url(r'^$', views.AthleteView, name='index'),

]