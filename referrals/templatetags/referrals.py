from django import template
from ..models import Link
from django.core.cache import cache
from django.conf import settings


register = template.Library()


@register.inclusion_tag('referrals/referral_input.html', takes_context=True)
def input(context):
    address = settings.DJANGO_REFERRALS_DEFAULT_URL

    request = context.get('request', None)
    if request:
        if request.user.is_authenticated:
            user = context['request'].user

            if '{}_referral_link'.format(user.id) in cache:
                token = cache.get('{}_referral_link'.format(user.id))
            else:
                link, created = Link.objects.get_or_create(user=user)
                token = link.token
                cache.set(
                    '{}_referral_link'.format(user.id),
                    '{}'.format(token),
                    60*60*24*30
                )
            return {
                'link': '{}?ref={}'.format(address, token)
            }

    default_token = settings.DJANGO_REFERRALS_DEFAULT_INPUT_VALUE
    return {
        'link': '{}?ref={}'.format(address, default_token)
    }


@register.simple_tag(takes_context=True)
def token(context):
    address = settings.DJANGO_REFERRALS_DEFAULT_URL

    request = context.get('request', None)
    if request:
        if request.user.is_authenticated:
            user = context['request'].user

            if '{}_referral_link'.format(user.id) in cache:
                token = cache.get('{}_referral_link'.format(user.id))
            else:
                link, created = Link.objects.get_or_create(user=user)
                token = link.token
                cache.set(
                    '{}_referral_link'.format(user.id),
                    '{}'.format(token),
                    60*60*24*30
                )
            return '{}?ref={}'.format(address, token)

    default_token = settings.DJANGO_REFERRALS_DEFAULT_INPUT_VALUE
    return '{}?ref={}'.format(address, default_token)
