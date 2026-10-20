.. :changelog:

History
-------

0.3 (2026-10-21)
++++++++++++++++++

* README: the signal examples were not valid Python. ``.send(sender=User,
  request, user)`` is a SyntaxError, because Python does not allow positional
  arguments after a keyword argument. Two issues were filed against this
  package because of it. The examples are fixed and a test now checks that
  every python block in the README parses.
* README: the ``INSTALLED_APPS`` and ``urlpatterns`` examples were missing a
  comma after the ``...`` placeholder and did not parse either.
* README: ``DJANGO_REFERRALS_DEFAULT_INPUT_VALUE`` was documented with a
  concrete uuid that people copy-pasted. It has to be the token of a
  ``Link`` row that already exists, otherwise the receiver finds no link and
  records nothing. The placeholder is now explicit about that.
* Fix the referral token being lost when the signup form is posted to a URL
  without the query string. The token is now also read from the ``ref``
  parameter of the ``Referer`` header, which is the usual case: the user
  arrives on ``?ref=<token>`` and then submits the form.
* README: the usage example referred to an undefined ``SignupForm``. It now
  shows a complete form and states that the field has to be named
  ``referral``, and documents the django-allauth variant.
* Packaging: ``project.license`` moved to the SPDX expression, the deprecated
  license classifier removed, package discovery switched to ``find`` so
  ``referrals.migrations`` is not silently left out.
* Add a GitHub Actions workflow that publishes to PyPI through Trusted
  Publishing (OIDC), so no API token has to be stored in the repository.
* Support Django 4.2, 5.x and 6.x on Python 3.9+. Drop support for Django < 4.2 and Python < 3.9.
* Remove Python 2 compatibility shims(``python_2_unicode_compatible``, ``ugettext_lazy``, ``default_app_config``).
* ``Signal(providing_args=...)`` was removed in Django 4.0, the arguments are now inferred from receivers.
* Replace ``setup.py`` with ``pyproject.toml`` (PEP 621).
* Drop the ``django-environ`` pin; it was only used by the example project.
* Delete the drifted duplicate copy of the app under ``example/``; the example now uses the installed package.
* Django 6.0 changed ``DEFAULT_AUTO_FIELD`` from ``AutoField`` to
  ``BigAutoField``. The auto-created primary keys are never declared in the
  models, so every existing install on Django 6 was handed three pointless
  ``AlterField`` operations for keys this app never changes. Pinned to
  ``AutoField`` in ``ReferralsConfig`` to match the shipped migration.
* Replace Travis CI with GitHub Actions.
* Rewrite CONTRIBUTING.rst, which still described the project as ``django-referrals``
  under a previous GitHub username and instructed contributors to run removed
  commands (``setup.py develop``, ``setup.py test``, ``tox``).
* The docs on Read the Docs were building with errors: three literal blocks in
  ``README.rst`` were malformed and mixed bullet markers broke the Features
  list, and ``docs/usage.rst`` documented ``django.conf.urls.url`` plus a
  namespaceless ``include``. The docs now build clean under ``-W``, duplicate
  ``installation.rst``/``usage.rst`` were dropped in favour of the README, and
  CI builds the docs so this cannot regress.

0.1.0 (2018-04-13)
++++++++++++++++++

* First release on PyPI.
