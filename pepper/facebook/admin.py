# Third Party imports
from django.contrib import admin

# Register your models here.
from pepper.facebook.models import PSIDList, FacebookPage, MessengerLabel


@admin.register(FacebookPage)
class FacebookPageAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Information', {
            'fields': (
                'owner', 'page_name', 'page_id', 'access_token',
            )
        }),
    )


@admin.register(MessengerLabel)
class MessengerLabelAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Information', {
            'fields': (
                'owner', 'page', 'label_name', 'label_id',
            )
        }),
    )


@admin.register(PSIDList)
class PSIDListAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Information', {
            'fields': (
                'page', 'label', 'psid_list', 'valid_psid', 'invalid_psid', 'label_associated_to',
            )
        }),
    )
