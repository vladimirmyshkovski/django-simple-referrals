from test_plus.test import TestCase
from referrals.templatetags import referrals
from django.template import Context, Template
from django.test import RequestFactory
from bs4 import BeautifulSoup
from referrals.models import Link
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.core.cache import cache
import random


class TestToken(TestCase):

	def setUp(self):
		self.user = self.make_user('user-{}'.format(random.randint(1, 100)))
	
	def test_with_user(self):
		request_factory = RequestFactory()
		request = request_factory.get('/?ref=123123123')
		request.user = self.user
		
		out = Template(
			"{% load referrals %}"
			"{% token %}"
		).render(Context({
			'request': request,
			'user': self.user
			}
		))
		
		soup = BeautifulSoup(out, 'html.parser')
		address = settings.DJANGO_REFERRALS_FORM_URL
		
		link = Link.objects.get(user=self.user)
		
		self.assertEqual(
			soup.find('form').find('input').get('value'),
			'{}?ref={}'.format(address, link.token)
		)
	
	def test_without_user(self):
		request_factory = RequestFactory()
		request = request_factory.get('/?ref=123123123')
		request.user = AnonymousUser()

		out = Template(
			"{% load referrals %}"
			"{% token %}"
		).render(Context({
			'request': request,
			'user': self.user
			}
		))

		soup = BeautifulSoup(out, 'html.parser')
		address = settings.DJANGO_REFERRALS_FORM_URL
		default_token = settings.DJANGO_REFERRALS_DEFAULT_INPUT_VALUE

		self.assertEqual(
			soup.find('form').find('input').get('value'),
			'{}?ref={}'.format(address, default_token)
		)
	
	def test_cache(self):
		request_factory = RequestFactory()
		request = request_factory.get('/?ref=123123123')
		request.user = self.user

		out = Template(
			"{% load referrals %}"
			"{% token %}"
		).render(Context({
			'request': request,
			'user': self.user
			}
		))
		
		link_from_db = Link.objects.get(user=self.user)
		link_from_cache = cache.get('{}_referral_link'.format(self.user))
		
		self.assertEqual(
			str(link_from_db.token),
			link_from_cache
		)
		
		link_from_db.delete()

		out = Template(
			"{% load referrals %}"
			"{% token %}"
		).render(Context({
			'request': request,
			'user': self.user
			}
		))

		soup = BeautifulSoup(out, 'html.parser')
		address = settings.DJANGO_REFERRALS_FORM_URL

		self.assertEqual(
			soup.find('form').find('input').get('value'),
			'{}?ref={}'.format(address, link_from_cache)
		)