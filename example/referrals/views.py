from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from .models import FlatReferral


class FlatReferralDetailView(LoginRequiredMixin, DetailView):

	model = FlatReferral
	template_name = 'referrals/flat_referral_detail.html'


class FlatReferralListView(LoginRequiredMixin, ListView):

	model = FlatReferral
	template_name = 'referrals/flat_referral_list.html'
	context_object_name = 'flat_referral_list'
	paginate_by = 10

	def get_queryset(self):
		queryset = super(FlatReferralListView, self).get_queryset()
		return queryset.filter(referrer=self.request.user).all()