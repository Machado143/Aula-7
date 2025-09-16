from django.forms import ModelForm, ValidationError
from . import models

class PostForm(ModelForm):
    class Meta:
        model = models.Post
        exclude = ['aprovado']

    def clean_mensagem(self):
        data = self.cleaned_data["mensagem"]
        if len(data) < 10:
            raise ValidationError("Precisa ter mais de 10 caracteres!")
        # Tirar espaços extra
        data = str(data).strip()
        return data

