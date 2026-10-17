============
Installation
============

At the command line::

    $ pip install django-simple-referrals

Add it to your ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'referrals',
        ...
    )

Then include the URL patterns:

.. code-block:: python

    from django.urls import include, path


    urlpatterns = [
        ...
        path('referrals/', include('referrals.urls', namespace='referrals')),
        ...
    ]

Referral links are then available as ``<DJANGO_REFERRALS_DEFAULT_URL>?ref=<token>``;
see the main README for the template tags and signals.