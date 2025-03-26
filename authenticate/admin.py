from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import custumuser  # Note the relative import


class CustomUserAdmin(UserAdmin):
    # Add all fields you want to display in the admin
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('full_name',)}),  # Add full_name here
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Custom Fields', {'fields': ('role',)}),  # Your custom role field
    )

    # Fields shown when creating a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'full_name', 'role'),
        }),
    )

    list_display = ('username', 'full_name', 'role', 'is_staff')
    search_fields = ('username', 'full_name')
    ordering = ('username',)

    def save_model(self, request, obj, form, change):
        """
        Assign the correct group based on role and remove old groups.
        """
        super().save_model(request, obj, form, change)  # Save user first

        obj.groups.clear()  # Remove existing groups

        role_to_group = {
            'admin': 'Admin',
            'gtu_cordinator': 'GTU Coordinator',
            'department': 'Department'
        }

        group_name = role_to_group.get(obj.role)
        if group_name:
            group, _ = Group.objects.get_or_create(name=group_name)
            obj.groups.add(group)  # Assign the correct group


admin.site.register(custumuser, CustomUserAdmin)