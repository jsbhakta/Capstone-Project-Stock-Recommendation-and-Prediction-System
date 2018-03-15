"""Defines URL patterns for stocks"""
from django.conf.urls import url
from stocks.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Home page
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^home/$', HomeView.as_view(), name='home'),
    #Disclaimer
    url(r'^q_disclaimer/$', q_disclaimer.as_view(), name='q_disclaimer'),
    #Questionnaire
    url(r'^q_start/$', q_start.as_view(), name='q_start'),
    url(r'^q_formB/$', B_form.as_view(), name='q_formB.'),

    #url(r'^q_resultF/$',views.q_resultF, name='q_resultF'),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)