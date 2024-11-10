from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'name', 'ph_num', 'is_staff', 'is_active', 'collected_stickers')
    search_fields = ('email', 'name', 'ph_num')
    list_filter = ('is_staff', 'is_active')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'ph_num')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'ph_num', 'password1', 'password2', 'is_active', 'is_staff')},
        ),
    )

    ordering = ('email',)

    def has_add_permission(self, request):
        return False

    def collected_stickers(self, obj):
        """Display collected stickers in admin as a list of IDs or names (based on your model setup)."""
        stickers = obj.collected_stickers()
        return ", ".join([str(sticker) for sticker in stickers]) if stickers else "No stickers"

    collected_stickers.short_description = 'Collected Stickers'


admin.site.register(User, UserAdmin)
