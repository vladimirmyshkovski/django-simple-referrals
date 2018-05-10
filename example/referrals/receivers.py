from .models import Link, FlatReferral, MultiLevelReferral
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from .signals import create_flat_referral, create_multi_level_referral
import logging


logger = logging.getLogger(__name__)


@receiver(create_flat_referral, sender=get_user_model())
def save_flat_referral(sender, request, user, **kwargs):

    referral_link = request.POST.get('referral', None)
    if not referral_link:
        referral_link = request.GET.get('ref', None)

    try:
        if referral_link:
            link = Link.objects.get(token=referral_link)
            FlatReferral.objects.create(
                referrer=link.user,
                referred=user
            )
    except Link.DoesNotExist:  # pragma: no cover
        logger.exception(
            'Link with token = {} does not exist'.format(referral_link))
    except ValidationError:  # pragma: no cover
        logger.exception('{} is not a valid Link.token'.format(referral_link))


@receiver(create_multi_level_referral, sender=get_user_model())
def save_multi_level_referral(sender, request, user, position, **kwargs):
    if position is not 'child' and position is not 'sibling':
        logger.exception('{} was sent instead of a child or brother'.format(
            position))  # pragma: no cover
        raise KeyError('Position can be child or sibling')  # pragma: no cover

    referral_link = request.POST.get('referral', None)
    if not referral_link:
        referral_link = request.GET.get('ref', None)
    try:
        if referral_link:
            link = Link.objects.get(token=referral_link)
            try:
                referral = MultiLevelReferral.objects.get(user=link.user)
                if position == 'sibling':
                    referral.add_sibling(user=user)
                else:
                    referral.add_child(user=user)
            except MultiLevelReferral.DoesNotExist:  # pragma: no cover
                logger.exception(
                    'MultiLevelReferral with user = {} does not exist'.format(
                        link.user
                    )
                )
    except Link.DoesNotExist:  # pragma: no cover
        logger.exception(
            'Link with token = {} does not exist'.format(referral_link))
    except ValidationError:  # pragma: no cover
        logger.exception('{} is not a valid Link.token'.format(referral_link))
