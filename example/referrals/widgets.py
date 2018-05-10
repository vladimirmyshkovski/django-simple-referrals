from django.forms.widgets import Widget
from django.template import loader
from django.utils.safestring import mark_safe
import environ


env = environ.Env()


class ReferralWidget(Widget):
    template_name = 'referrals/referral_widget_min.html'

    def get_context(self, name, value, attrs=None):
        default_token = env(
            'DJANGO_REFERRALS_DEFAULT_INPUT_VALUE',
            default='40ed41dc-d291-4358-ae4e-d3c07c2d67dc'
        )
        return {
            'widget': {
                'name': name,
                'value': value,
                'default_value': default_token
            }
        }

    def render(self, name, value, renderer=None, attrs=None):
        context = self.get_context(name, value, attrs)
        template = loader.get_template(self.template_name).render(context)
        return mark_safe(template)
