from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.base import ContextMixin
from django.core.exceptions import PermissionDenied
from django.conf import settings

from .models import FlatReferral, MultiLevelReferral


class FlatReferralDetailView(LoginRequiredMixin, DetailView):

    model = FlatReferral
    template_name = 'referrals/flat_referral_detail.html'

    def get_object(self, queryset=None):
        obj = super(FlatReferralDetailView, self).get_object(queryset=None)
        if obj.referrer == self.request.user or \
           obj.referred == self.request.user:
            return obj
        else:
            raise PermissionDenied()


class FlatReferralListView(LoginRequiredMixin, ListView):

    model = FlatReferral
    template_name = 'referrals/flat_referral_list.html'
    context_object_name = 'flat_referral_list'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(FlatReferralListView, self).get_queryset()
        return queryset.filter(referrer=self.request.user).all()


class MultiLevelReferralDetailView(LoginRequiredMixin, DetailView):

    model = MultiLevelReferral
    template_name = 'referrals/multi_level_referral_detail.html'

    def get_object(self, queryset=None):
        obj = super(MultiLevelReferralDetailView,
                    self).get_object(queryset=None)
        referrer = MultiLevelReferral.objects.get(user=self.request.user)
        if obj.is_descendant_of(referrer) or obj.user == self.request.user:
            return obj
        else:
            raise PermissionDenied()


class MultiLevelReferralListView(LoginRequiredMixin, ListView):

    model = MultiLevelReferral
    template_name = 'referrals/multi_level_referral_list.html'
    context_object_name = 'multi_level_referral_list'
    paginate_by = 10

    def get_queryset(self):
        descendants = self.request.user.multilevelreferral.get_descendants()
        descendants_ids = [descendant.id for descendant in descendants]
        queryset = super(MultiLevelReferralListView, self).get_queryset()
        #referrer = MultiLevelReferral.objects.get(user=self.request.user)
        #return referrer.get_descendants()
        return queryset.filter(id__in=descendants_ids)


class JavaScriptCode(TemplateView, ContextMixin):

    content_type = 'application/javascript'
    template_name = 'referrals/referral_script.js'

    def get_context_data(self, **kwargs):
        context = super(JavaScriptCode, self).get_context_data(**kwargs)
        default_value = settings.DJANGO_REFERRALS_DEFAULT_INPUT_VALUE
        prefix = settings.DJANGO_REFERRALS_PREFIX
        context['default_value'] = default_value
        context['prefix'] = prefix
        return context
