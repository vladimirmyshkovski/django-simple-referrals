# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from referrals.urls import urlpatterns as referrals_urls

urlpatterns = [
    url(r'^referrals/', include((referrals_urls, 'referrals'), namespace='referrals')),
]
