from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import custumuser  # Ensure correct import

class CustomUserAdmin(UserAdmin):
    fieldsets = list(UserAdmin.fieldsets) + [
        ("Custom Fields", {"fields": ("role",)}),  # Keep only 'role'
    ]

    def save_model(self, request, obj, form, change):
        """
        Assign the correct group based on role and remove old groups.
        """
        super().save_model(request, obj, form, change)  # Save user first

        obj.groups.clear()  # Remove existing groups

        role_to_group = {
            'admin': 'admin',
            'gtu_cordinator': 'gtu_cordinator',
            'department': 'department'
        }

        group_name = role_to_group.get(obj.role)
        if group_name:
            group, _ = Group.objects.get_or_create(name=group_name)
            obj.groups.add(group)  # Assign the correct group

admin.site.register(custumuser, CustomUserAdmin)  # 
