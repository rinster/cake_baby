from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.index),
    url(r'^portfolio$', views.portfolio),
    url(r'^cakeRequest$', views.cakeRequest),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^loginProcess$', views.loginProcess),
    url(r'^admin_page$', views.admin_page),
    url(r'^delete/(?P<id>\d+)$', views.delete),  
    url(r'^logout$', views.logout),
    url(r'^search$', views.search),

    url(r'^img_page$', views.img_page),
    url(r'^img_upload$', views.img_upload),
    url(r'^test$', views.test),
]                           
