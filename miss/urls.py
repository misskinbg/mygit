# miss/urls.py


from django.conf.urls import include, url

import miss.views as views


urlpatterns = [
    url(r'^$', views.login, name='login'),

    url(r'find/$', views.find, name='find'),
    url(r'logout/$', views.logout, name='logout'),

    url(r'aa1/$', views.aa1, name='aa1'),
    url(r'aa2/$', views.aa2, name='aa2'),
    url(r'aa3/$', views.aa3, name='aa3'),
    url(r'aa4/$', views.aa4, name='aa4'),
    url(r'aa5/$', views.aa5, name='aa5'),
    url(r'aa6/$', views.aa6, name='aa6'),
    url(r'aa7/$', views.aa7, name='aa7'),
    url(r'aa8/$', views.aa8, name='aa8'),
    url(r'aa9/$', views.aa9, name='aa9'),
    url(r'aa10/$', views.aa10, name='aa10'),
    url(r'admin/$', views.admin, name='admin'),



]