from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import User

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'phone', 'cpf', 'photo', 'email')


class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'phone', 'cpf', 'photo', 'email')


email = AuthenticationForm.base_fields['username']
password = AuthenticationForm.base_fields['password']
email.widget.attrs['class'] = password.widget.attrs['class'] = 'form-control login__input'
