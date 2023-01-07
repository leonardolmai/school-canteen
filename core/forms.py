from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import User

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'phone', 'cpf', 'photo', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form__input'


class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'phone', 'cpf', 'photo', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form__input'

login_email = AuthenticationForm.base_fields['username']
login_password = AuthenticationForm.base_fields['password']
login_email.widget.attrs['class'] = login_password.widget.attrs['class'] = 'form-control login__input'
