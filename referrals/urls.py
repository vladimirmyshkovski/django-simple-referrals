# -*- coding: utf-8 -*-
from django.urls import re_path

from . import views


app_name = 'referrals'
urlpatterns = [
    re_path(
        r'^$',
        view=views.JavaScriptCode.as_view(),
        name='javascript_code'
    ),
    re_path(
        r'^flat-referrals/$',
        view=views.FlatReferralListView.as_view(),
        name='flat_referral_list'
    ),
    re_path(
        r'^flat-referrals/(?P<pk>\d+)/$',
        view=views.FlatReferralDetailView.as_view(),
        name='flat_referral_detail'
    ),
    re_path(
        r'^multi-level-referrals/$',
        view=views.MultiLevelReferralListView.as_view(),
        name='multi_level_referral_list'
    ),
    re_path(
        r'^multi-level-referrals/(?P<pk>\d+)/$',
        view=views.MultiLevelReferralDetailView.as_view(),
        name='multi_level_referral_detail'
    )
]
