from django.forms.renderers import DjangoTemplates, Jinja2
from test_plus.test import TestCase
from referrals import widgets, fields
from django import forms
from django.template import Context, Template, TemplateSyntaxError
from django.test import RequestFactory


class Form(forms.Form):
	referral = fields.ReferralField(widget = widgets.ReferralWidget())


try:
    import jinja2
except ImportError:
	jinja2 = None


TestCase.maxDiff = None


class ReferralWidgetTest(TestCase):

	@classmethod
	def setUpClass(cls):
		cls.django_renderer = DjangoTemplates()
		cls.jinja2_renderer = Jinja2() if jinja2 else None
		cls.renderers = [cls.django_renderer] + ([cls.jinja2_renderer] if cls.jinja2_renderer else [])
		super().setUpClass()

	def check_html(self, widget, name, value, html='', attrs=None, strict=False, **kwargs):
		assertEqual = self.assertEqual if strict else self.assertHTMLEqual
		if self.jinja2_renderer:
			output = widget.render(name, value, attrs=attrs, renderer=self.jinja2_renderer, **kwargs)
			# Django escapes quotes with '&quot;' while Jinja2 uses '&#34;'.
			assertEqual(output.replace('&#34;', '&quot;'), html)

		output = widget.render(name, value, attrs=attrs, renderer=self.django_renderer, **kwargs)
		assertEqual(output, html)

	def test_render(self):
		widget = widgets.ReferralWidget()
		html = '''<input id="id-referral" type="hidden" name="referral" value="TEST"><script type="text/javascript">window.onload=function(){var getUrlParameter=function getUrlParameter(sParam){var sPageURL=decodeURIComponent(window.location.search.substring(1)), sURLVariables=sPageURL.split('&'), sParameterName, i; for (i=0; i < sURLVariables.length; i++){sParameterName=sURLVariables[i].split('='); if (sParameterName[0]===sParam){return sParameterName[1]===undefined ? true : sParameterName[1];}}};var referralLink=getUrlParameter('ref');var referral=localStorage.getItem('referralLink');if (typeof referralLink !=="undefined"){localStorage.setItem('referralLink', referralLink)};if (typeof referral==="undefined" || referral===null){localStorage.setItem('referralLink', 'TEST' )};var signUpReferralLink=localStorage.getItem('referralLink');document.getElementById('id-referral').value=signUpReferralLink;}</script>'''	
		attrs = {
			'type': 'hidden',
			'id':'id-referral',
		}
		self.check_html(widgets.ReferralWidget(), 'referral', 'TEST', html = html, attrs = attrs)

	def test_js(self):
		request_factory = RequestFactory()
		out = Template(
			"{{ form }}"
		).render(Context({
			'request': request_factory.get('/?ref=123123123'),
			'form': Form()
			}))
		