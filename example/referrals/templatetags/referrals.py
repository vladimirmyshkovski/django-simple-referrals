from django import template
from ..models import Link
from django.conf import settings
from django.core.cache import cache


register = template.Library()


@register.inclusion_tag('referrals/referral_token.html', takes_context=True)
def token(context):
	address = settings.DJANGO_REFERRALS_FORM_URL

	if context['request'].user.is_authenticated:
		user = context['request'].user

		if '{}_referral_link'.format(user) in cache:
			token = cache.get('{}_referral_link'.format(user)) 
		else:
			link, created = Link.objects.get_or_create(user=user)
			token = link.token
			cache.set(
				'{}_referral_link'.format(user),
				'{}'.format(token),
				60*60*24
			)
		return {
			'link': '{}?ref={}'.format(address, token)
		}
	
	default_token = settings.DJANGO_REFERRALS_DEFAULT_INPUT_VALUE
	return {
		'link': '{}?ref={}'.format(address, default_token)
	}