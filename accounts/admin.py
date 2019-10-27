from django.contrib import admin
from .models import Grade, Location, OrgType
from .models import Organization, OrganizationAdmin


admin.site.register(Grade)
admin.site.register(Location)
admin.site.register(OrgType)
admin.site.register(Organization, OrganizationAdmin)

