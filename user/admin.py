from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'first_name',)
    list_filter = ('groups', 'is_active', 'is_staff',
                   'is_superuser', 'email', 'username',
                   )
    ordering = ('-date_joined',)
    list_display = ('email', 'username', 'first_name', 'is_active', 'is_staff', 'id',)
    fieldsets = (
        ('Login', {'fields': ('email', 'username', 'password',)}),
        ('Personal', {'fields': ('first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
        ('Groups', {'fields': ('groups',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'username', 'password1', 'password2',
                'first_name', 'last_name', 'is_active',
                'is_staff', 'groups')
        }
         ),
    )


admin.site.register(User, UserAdminConfig)
