#from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
import django.dispatch
import logging
from .models import Link, FlatReferral, MultiLevelReferral
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


logger = logging.getLogger(__name__)


create_flat_referral = django.dispatch.Signal(providing_args=["request", "user"])
create_multi_level_referral = django.dispatch.Signal(providing_args=["request", "user", "position"])



@receiver(create_flat_referral, sender=None)
def save_flat_referral(sender, request, user, **kwargs):

	referral_link = request.POST.get('referral', None)
	if not referral_link:
		referral_link = request.GET.get('ref', None)

	try:
		if referral_link:
			link = Link.objects.get(token = referral_link)
			referral = FlatReferral.objects.create(
				referrer = link.user,
				referred = user
			)
	except Link.DoesNotExist: # pragma: no cover
		logger.exception('Link with token = {} does not exist'.format(referral_link))
	except ValidationError: # pragma: no cover
		logger.exception('{} is not a valid Link.token'.format(referral_link))


'''
@receiver(post_save, sender=get_user_model())
def create_link(sender, instance. created, **kwargs):
	if created:
		Link.objects.create(user=instance)

'''

@receiver(create_multi_level_referral, sender=None)
def save_multi_level_referral(sender, request, user, position, **kwargs):
	if position is not 'child' and position is not 'sibling':
		logger.exception('{} was sent instead of a child or brother'.format(position)) # pragma: no cover
		raise KeyError('Position can be child or sibling') # pragma: no cover
	
	referral_link = request.POST.get('referral', None)
	if not referral_link:
		referral_link = request.GET.get('ref', None)
	try: 
		if referral_link:
			link = Link.objects.get(token = referral_link)
			try:
				referral = MultiLevelReferral.objects.get(user = link.user)
				if position == 'sibling':
					referral.add_sibling(user = user)
				else:
					referral.add_child(user = user)
			except MultiLevelReferral.DoesNotExist: # pragma: no cover
				logger.exception('MultiLevelReferral with user = {} does not exist'.format(link.user))
	except Link.DoesNotExist: # pragma: no cover
		logger.exception('Link with token = {} does not exist'.format(referral_link))
	except ValidationError: # pragma: no cover
		logger.exception('{} is not a valid Link.token'.format(referral_link))