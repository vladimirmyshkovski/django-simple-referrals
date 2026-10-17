# -*- coding: utf-8 -*-

from django.urls import include, re_path

from referrals.urls import urlpatterns as referrals_urls

urlpatterns = [
    re_path(r'^referrals/', include((referrals_urls, 'referrals'), namespace='referrals')),
]
