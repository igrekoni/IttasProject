from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from mainpage import views


urlpatterns = [
    url(r'^$', views.mainpage, name='mainpage'),
    url(r'^admin/', admin.site.urls),
    url(r'^contacts/', views.contacts, name='contacts'),
    url(r'^news/', include("news.urls", namespace='news')),

    url(r'^solutions/scna/', views.scna, name='scna'),
    url(r'^solutions/cna/', views.cna, name='cna'),
    url(r'^solutions/d-key/', views.dkey, name='dkey'),

    url(r'^laboratory/attestation/', views.attestation, name='attestation'),
    url(r'^laboratory/sertification/', views.sertification, name='sertification'),
    url(r'^laboratory/ekspertiza/', views.ekspertiza, name='ekspertiza'),
    url(r'^laboratory/oblast-akkreditacii/', views.oblast, name='oblast-akkreditacii'),

    url(r'^company/audit-is/', views.audit, name='audit-is'),
    url(r'^company/soprovozhdenie-po/', views.soprovozhdenie, name='soprovozhdenie-po'),
    url(r'^company/razrabotka-programmnogo-obespecheniya/', views.razrabotka, name='razrabotka-programmnogo-obespecheniya'),
    url(r'^company/o-kompanii/', views.company, name='o-kompanii'),

    url(r'^vacancies/', views.vacancies, name='vacancies'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)