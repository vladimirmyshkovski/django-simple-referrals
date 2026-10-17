"""Sphinx configuration for django-simple-referrals.

The docs are intentionally thin: they are the README plus the project
metadata files. Every page is an ``include``, so there is no second copy of
the documentation to drift out of sync.
"""

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

import referrals  # noqa: E402

project = "django-simple-referrals"
author = "Vladimir Myshkovski"
copyright = "2018-2026, Vladimir Myshkovski"  # noqa: A001

version = referrals.__version__
release = referrals.__version__

extensions = ["sphinx.ext.autodoc", "sphinx.ext.viewcode"]

source_suffix = ".rst"
master_doc = "index"
exclude_patterns = ["_build"]

pygments_style = "sphinx"
html_theme = "alabaster"

htmlhelp_basename = "django_simple_referralsdoc"
