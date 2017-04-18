from django.conf.urls import url, include
from django.contrib import admin
from mainpage import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^contacts/', views.contacts, name='contacts'),
    url(r'^$', views.mainpage, name='mainpage'),
    url(r'^solutions/scna/', views.scna, name='scna'),
    url(r'^solutions/cna/', views.cna, name='cna'),
    url(r'^solutions/d-key/', views.dkey, name='dkey'),


    url(r'^laboratory/attestation/', views.attestation, name='attestation'),
    url(r'^laboratory/sertification/', views.sertification, name='sertification'),


]
