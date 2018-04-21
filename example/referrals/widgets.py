from django.forms.widgets import Widget
from django.template import loader
from django.utils.safestring import mark_safe
from django.conf import settings


class ReferralWidget(Widget):
	template_name = 'referrals/referral_widget_min.html'

	def get_context(self, name, value, attrs=None):
		return {
			'widget': {
				'name': name,
				'value': value,
				'default_value': settings.DJANGO_REFERRALS_DEFAULT_INPUT_VALUE
			}
		}

	def render(self, name, value, renderer=None, attrs=None):
		context = self.get_context(name, value, attrs)
		template = loader.get_template(self.template_name).render(context)
		return mark_safe(template)