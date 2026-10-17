.. :changelog:

History
-------

0.3 (2026-10-17)
++++++++++++++++++

* Support Django 4.2, 5.x and 6.x on Python 3.9+. Drop support for Django < 4.2 and Python < 3.9.
* Remove Python 2 compatibility shims(``python_2_unicode_compatible``, ``ugettext_lazy``, ``default_app_config``).
* ``Signal(providing_args=...)`` was removed in Django 4.0, the arguments are now inferred from receivers.
* Replace ``setup.py`` with ``pyproject.toml`` (PEP 621).
* Drop the ``django-environ`` pin; it was only used by the example project.
* Delete the drifted duplicate copy of the app under ``example/``; the example now uses the installed package.
* Replace Travis CI with GitHub Actions.
* Rewrite CONTRIBUTING.rst, which still described the project as ``django-referrals``
  under a previous GitHub username and instructed contributors to run removed
  commands (``setup.py develop``, ``setup.py test``, ``tox``).

0.1.0 (2018-04-13)
++++++++++++++++++

* First release on PyPI.
