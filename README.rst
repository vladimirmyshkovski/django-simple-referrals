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

There are two types of referral structure: flat and multilevel.

A flat structure means that the user can have referrals, and they will all be on the same level.

Multilevel structure means that the user can have children who, in turn, also have children, each of which will be on a level lower (deeper) than the parent.


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



Usage
----------

1) Override your SignupForm

.. code-block:: python

    from referrals.widgets import ReferralWidget
    from referrals.fields import ReferralField

    class ReferralSignupForm(SignupForm):

        referral = ReferralField(widget=ReferralWidget())



2) After registration, send a signal

If you want to use a flat structure:

.. code-block:: python

    from referrals.signals import create_flat_referral

    create_flat_referral.send(sender=User, request, user)



Or, if you want to use a multi-level structure

.. code-block:: python

    from referrals.signals import create_multi_level_referral

    create_flat_referral.send(sender=User, request, user, 'position')



Where the 'position' must be 'child' or 'sibling'

If you pass the value "child", then a child will be created from the referral, by whose link the user has registered.

If you specify "sibling", you will create a referral that is at the same level as the user whose link the user is registered with.

3) Template tags with referral link:
::
    {% referrals %} # Import template tags

    {% token %} # Use in any place in your html code

An incompromise will be created with the button "Copy" by clicking on it, the referral link of this user will be copied to the clipboard.

4) Export default variables:

.. code-block:: python

    export DJANGO_REFERRALS_DEFAULT_INPUT_VALUE = '40ed41dc-d291-4358-ae4e-d3c07c2d67dc' # The token to be used by
                                                                                         # default. WARNING: Must be uuid4 
    
    export DJANGO_REFERRALS_FORM_URL = 'http://localhost:8000/accounts/signup/'          # The signup URL





Features
--------

* TODO
- Create a class for extracting the defaul UUID token
- Eliminate a possible error, with a non uuid4 format token

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
