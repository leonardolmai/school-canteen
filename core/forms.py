from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'phone', 'cpf', 'photo', 'email')


class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'phone', 'cpf', 'photo', 'email')
