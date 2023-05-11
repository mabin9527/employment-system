from django import forms


class BootStrapModelFrom(forms.ModelForm):
    """
    BootStrapModelForm class provides django forms css style and js.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] = field.label

            else:
                field.widget.attrs = {
                    'class': 'form-control'
                    'placeholder': field.label
                }