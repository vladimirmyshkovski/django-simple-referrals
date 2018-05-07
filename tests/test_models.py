#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-referrals
------------

Tests for `django-referrals` models module.
"""

from test_plus.test import TestCase
from django.core.exceptions import ValidationError

from referrals import models


class TestReferral(TestCase):

    def setUp(self):
        self.first_user = self.make_user('u1')
        self.second_user = self.make_user('u2')
        self.third_user = self.make_user('u3')
        self.referral = models.FlatReferral.objects.create(
            referrer=self.first_user,
            referred=self.second_user
        )

    def test__str__(self):
        self.assertEqual(
            self.referral.__str__(),
            '{} => {}'.format(self.first_user, self.second_user)
        )

    def test_get_absolute_url(self):
        self.assertEqual(
            self.referral.get_absolute_url(),
            '/referrals/flat-referrals/1/'
        )

    def test_clean(self):
        self.assertRaises(
            ValidationError,
            lambda: models.FlatReferral.objects.create(
                referrer=self.first_user,
                referred=self.first_user
            )
        )

        self.assertRaisesMessage(
            ValidationError,
            'The referrer can not be referred.',
            lambda: models.FlatReferral.objects.create(
                referrer=self.first_user,
                referred=self.first_user
            )
        )

    def tearDown(self):
        pass


class TestMultiLevelReferral(TestCase):

    def setUp(self):
        self.root_user = self.make_user('root_user')
        self.root = models.MultiLevelReferral.add_root(user=self.root_user)

        self.child_1 = self.root.add_child(user=self.make_user('user-1'))
        self.child_2 = self.root.add_child(user=self.make_user('user-2'))

    def test__str__(self):
        self.assertEqual(
            self.root.__str__(),
            'root_user'
        )

    def test_get_absolute_url(self):
        self.assertEqual(
            self.root.get_absolute_url(),
            '/referrals/multi-level-referrals/1/'
        )
