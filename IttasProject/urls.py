from django.conf.urls import url, include
from django.contrib import admin
from mainpage import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^contacts/', views.contacts, name='contacts'),
    url(r'^$', views.mainpage, name='mainpage'),

]
