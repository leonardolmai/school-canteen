from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdmin_Django
from .forms import UserCreationForm, UserChangeForm
from .models import User
from django.utils.translation import gettext as _

# Register your models here.

class UserAdmin(UserAdmin_Django):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name', 'cpf', 'phone')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'cpf', 'phone', 'photo')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(User, UserAdmin)
