from django import forms
from .models import Product

class ProductModelForm(forms.ModelForm):
    validity = forms.DateField(
        label='Validade',
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={'type': 'date'}
        ),
        input_formats=('%Y-%m-%d',)
    )

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update(rows='3')
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form__input'
