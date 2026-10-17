============
Contributing
============

Contributions are welcome.

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/vladimirmyshkovski/django-simple-referrals/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* The Python and Django versions you are running.
* Detailed steps to reproduce the bug.

Get Started!
------------

1. Fork and clone the repo::

    $ git clone git@github.com:your_name_here/django-simple-referrals.git
    $ cd django-simple-referrals

2. Create a virtualenv and install the package with its test extras::

    $ python -m venv .venv
    $ . .venv/bin/activate
    $ pip install -e ".[test]"

3. Create a branch for your work::

    $ git checkout -b name-of-your-bugfix-or-feature

4. Make your changes, then check them::

    $ flake8 referrals tests
    $ python manage.py test tests

   Alternatively, ``make lint`` and ``make test`` do the same.

5. Commit and push, then open a pull request::

    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

Supported versions
------------------

Python 3.9 and above. Django 4.2, 5.x and 6.x are tested in CI; see
`.github/workflows/test.yml` for the exact matrix. Note that Django 5.2
requires Python 3.10+, Django 6.x requires Python 3.12+, and Django 4.2
is supported up to Python 3.12.

Pull Request Guidelines
-----------------------

1. The pull request should include tests.
2. If it adds functionality, update ``README.rst`` and the entry in
   ``HISTORY.rst``.
3. It must pass CI for the full matrix.
4. If it changes behaviour, say so explicitly in the description and
   consider whether it needs a deprecation path.