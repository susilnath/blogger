from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^view$', views.view_blog, name='view_it'),
    url(r'^create$', views.create_blog, name='create'),
    url(r'^submit$', views.submit_blog, name='submit'),
    url(r'^delete$', views.delete_blog, name='delete'),
    url(r'^edit$', views.edit_blog, name='edit'),
    
]