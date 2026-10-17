# -*- coding: utf-8
from django.apps import AppConfig


class ReferralsConfig(AppConfig):
    name = 'referrals'
    # Django 6.0 changed DEFAULT_AUTO_FIELD from AutoField to BigAutoField.
    # Pin it back so the shipped initial migration keeps matching the model
    # state: otherwise every existing install on Django 6 is handed three
    # pointless AlterField operations on primary keys this app never changes.
    # The auto_created pk is never declared in the models, so this is the only
    # place it can be pinned.
    default_auto_field = 'django.db.models.AutoField'
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
