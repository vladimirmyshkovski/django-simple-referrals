# -*- coding: utf-8
from django.apps import AppConfig


class ReferralsConfig(AppConfig):
    name = 'referrals'
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = 'Referrals'

    def ready(self):
        """Override this to put in:
                Referrals system checks
                Referrals signal registration
        """
        try:  # pragma: no cover
            import referrals.receivers  # noqa F401
        except ImportError:  # pragma: no cover
            pass
