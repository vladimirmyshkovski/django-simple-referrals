=============================
referrals
=============================

.. image:: https://badge.fury.io/py/django-referrals.svg
    :target: https://badge.fury.io/py/django-referrals

.. image:: https://travis-ci.org/narnikgamarnikus/django-referrals.svg?branch=master
    :target: https://travis-ci.org/narnikgamarnikus/django-referrals

.. image:: https://codecov.io/gh/narnikgamarnikus/django-referrals/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/narnikgamarnikus/django-referrals

A simple application that allows you to generate referral links and track referrals

Documentation
-------------

The full documentation is at https://django-referrals.readthedocs.io.

Quickstart
----------

Install referrals::

    pip install django-referrals

Add it to your `INSTALLED_APPS`:

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

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
