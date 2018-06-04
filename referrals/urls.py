# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views


app_name = 'referrals'
urlpatterns = [
    url(
        r'^$',
        view=views.JavaScriptCode.as_view(),
        name='javascript_code'
    ),
    url(
        r'^flat-referrals/$',
        view=views.FlatReferralListView.as_view(),
        name='flat_referral_list'
    ),
    url(
        r'^flat-referrals/(?P<pk>\d+)/$',
        view=views.FlatReferralDetailView.as_view(),
        name='flat_referral_detail'
    ),
    url(
        r'^multi-level-referrals/$',
        view=views.MultiLevelReferralListView.as_view(),
        name='multi_level_referral_list'
    ),
    url(
        r'^multi-level-referrals/(?P<pk>\d+)/$',
        view=views.MultiLevelReferralDetailView.as_view(),
        name='multi_level_referral_detail'
    )
]
