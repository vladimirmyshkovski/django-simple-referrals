from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import FlatReferral, Link, MultiLevelReferral

class MultiLevelReferralAdmin(TreeAdmin):
	form = movenodeform_factory(MultiLevelReferral)

admin.site.register(MultiLevelReferral, MultiLevelReferralAdmin)


admin.site.register(FlatReferral)
admin.site.register(Link)
