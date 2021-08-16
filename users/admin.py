from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import Profile

# Register your models here.
from django.contrib.auth.models import User

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'phone_number', 'web_site')

    list_display_links = ('id','user')

    search_fields = ('phone_number', 'user__username')

    list_filter = ('created', 'modified', 'user__is_active')

    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'), ),
        }),
        ('Extra Info', {
            'fields': (
                ('web_site','phone_number'),
                ('biography',),
            ),
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),)
        })
    )

    readonly_fields = ('created', 'modified')

class ProfileInLine(admin.StackedInline):

    model = Profile

    can_delete = False

    verbose_name_plural = 'Profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInLine,)

admin.site.unregister(User)

admin.site.register(User, UserAdmin)