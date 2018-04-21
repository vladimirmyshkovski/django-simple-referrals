=====
Usage
=====

To use referrals in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'referrals.apps.ReferralsConfig',
        ...
    )

Add referrals's URL patterns:

.. code-block:: python

    from referrals import urls as referrals_urls


    urlpatterns = [
        ...
        url(r'^', include(referrals_urls)),
        ...
    ]
