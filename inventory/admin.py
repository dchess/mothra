from django.contrib import admin
from .models import Domain, Subject, UsageType
from .models import Product, ProductAdmin
from .models import Usage, UsageAdmin


admin.site.register(Domain)
admin.site.register(Subject)
admin.site.register(UsageType)
admin.site.register(Product, ProductAdmin)
admin.site.register(Usage, UsageAdmin)
