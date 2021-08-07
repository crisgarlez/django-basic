from django.contrib import admin
from users.models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'phone_number', 'web_site')
    list_display_links = ('id','user')
    search_fields = ('phone_number', 'user__username')
    list_filter = ('created', 'modified', 'user__is_active')