=============================
Django-simple-referrals
=============================

.. image:: https://badge.fury.io/py/django-simple-referrals.svg
    :target: https://badge.fury.io/py/django-simple-referrals

.. image:: https://travis-ci.org/narnikgamarnikus/django-simple-referrals.svg?branch=master
    :target: https://travis-ci.org/narnikgamarnikus/django-simple-referrals

.. image:: https://codecov.io/gh/narnikgamarnikus/django-simple-referrals/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/narnikgamarnikus/django-simple-referrals

A simple application that allows you to generate referral links and track referrals

Documentation
-------------

The full documentation is at https://django-simple-referrals.readthedocs.io.

Quickstart
----------

Install referrals::

    pip install django-simple-referrals

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'referrals',
        ...
    )

Add referrals's URL patterns:

.. code-block:: python

    from referrals import urls as referrals_urls


    urlpatterns = [
        ...
        url(r'^referrals/', include('referrals_urls', namespace='referrals')),
        ...
    ]

Add to your settings file:

.. code-block:: python

    DJANGO_REFERRALS_DEFAULT_INPUT_VALUE = 'TEST' # The token to be used by default
    DJANGO_REFERRALS_FORM_URL = 'http://localhost:8000/accounts/signup/' # The signup form URL





Features
--------

* TODO
- Create a class for extracting the defaul UUID token

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
