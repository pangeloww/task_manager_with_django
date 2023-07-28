from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'created_at')
    list_filter = ('is_staff', 'created_at')
    ordering = ('-created_at',)
    search_fields = ('email', 'first_name', 'last_name')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'created_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )

    def assign_to_group(self, request, queryset):
        group_id = request.POST['group_id']  # The selected group's ID from the admin form
        group = Group.objects.get(pk=group_id)

        for user in queryset:
            user.groups.add(group)

        self.message_user(request, f"Selected users assigned to group: {group.name}")

    assign_to_group.short_description = "Assign selected users to a group"

    actions = [assign_to_group]  # Register the custom action


admin.site.register(User, CustomUserAdmin)
