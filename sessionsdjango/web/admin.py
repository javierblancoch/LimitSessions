from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin, Group
from .models import User, UserAcces

admin.site.register(User, UserAdmin)
UserAdmin.fieldsets += ('Custom fields', {'fields': ('description',)}),
admin.site.unregister(Group)

@admin.register(UserAcces)
class UserAccesAdmin(admin.ModelAdmin):
	list_display = ('id','user','session_key','datetime',)