from django import forms


class ReferralField(forms.CharField):

	def __init__(self, *args, **kwargs):
		super(ReferralField, self).__init__(*args, **kwargs)
		self.label = ''
