from urllib.parse import parse_qs, urlparse
from uuid import UUID


def extract_referral_token(request):
    """Find the referral token on a request.

    Looked for in the order a real signup flow provides it:

    1. ``POST['referral']`` - the hidden field rendered by
       ``ReferralWidget``.
    2. ``GET['ref']`` - the query string of the referral link itself.
    3. The ``ref`` query parameter of the ``Referer`` header - the user
       arrived on ``?ref=<token>`` and then submitted a form that posts to
       a URL without the query string, which is the usual case.
    """
    token = request.POST.get('referral', None)
    if not token:
        token = request.GET.get('ref', None)
    if not token:
        referer = request.META.get('HTTP_REFERER', '')
        token = parse_qs(urlparse(referer).query).get('ref', [None])[0]
    return token


def validate_uuid4(uuid_string):

    """
    Validate that a UUID string is in
    fact a valid uuid4.
    Happily, the uuid module does the actual
    checking for us.
    It is vital that the 'version' kwarg be passed
    to the UUID() call, otherwise any 32-character
    hex string is considered valid.
    """
    try:
        UUID(uuid_string, version=4)
    except ValueError:
        # If it's a value error, then the string
        # is not a valid hex code for a UUID.
        return False
    except TypeError:
        # If it's a type error, then the string
        # is None or something else
        return False

    return uuid_string
