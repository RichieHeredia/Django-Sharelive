from django.contrib import admin
from django.conf.urls import url , include 
from basic_app import views
from django.urls import path


urlpatterns = [
    url('^$', views.index , name= 'index'),
    url(r'^principal/$', views.principal, name='principal'),
    url(r'^admin/', admin.site.urls),
    #url('^basic_app/', include('basic_app.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^special/', views.special, name='special'),
    #url(r'^biblioteca/$', views.biblioteca, name='biblioteca'),
    url(r'^reproductor/$', views.reproductor, name='reproductor'),
    url(r'^formulario/$', views.formulario, name='formulario'),
    path('', include('basic_app.urls')),
]
