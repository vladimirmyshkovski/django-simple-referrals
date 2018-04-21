# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'referrals'
urlpatterns = [
    #url(r'', TemplateView.as_view(template_name="base.html")),
    url(
    	r'^$',
    	view = views.FlatReferralListView.as_view(),
    	name = 'flat_referral_list'
    ),
    url(
    	r'^(?P<pk>\d+)/$',
    	view = views.FlatReferralDetailView.as_view(),
    	name = 'flat_referral_detail'
    )
]
