from django.apps import apps
from django.test import TestCase
from referrals import apps as referrals_apps


class WalletsConfigTest(TestCase):

    def test_apps(self):
        self.assertEqual(referrals_apps.ReferralsConfig.name, 'referrals')
        self.assertEqual(apps.get_app_config('referrals').name, 'referrals')
        self.assertEqual(apps.get_app_config(
            'referrals').verbose_name, 'Referrals')
