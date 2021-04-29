from django.contrib import admin

from users.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.rest_apis.forms import UserChangeForm, UserCreationForm


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'full_name', 'is_active', 'is_admin', 'is_blocked', 'gender',)
    list_filter = ('is_admin', 'is_active', 'is_blocked')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', 'gender', 'date_of_birth')}),
        ('Permissions', {'fields': ('is_admin', 'is_active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',
                       'first_name', 'last_name', 'phone_number', 'gender', 'date_of_birth',
                       'is_active', 'is_admin',)
        }),
    )
    search_fields = ('email', 'phone_number', 'first_name')
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
