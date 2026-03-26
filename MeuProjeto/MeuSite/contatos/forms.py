from django import forms
from contatos.models import Pessoa

class ContatoModel2Form(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = "__all__"
    dtNascimento = forms.DateField(
        input_formats=["%d/%m/%Y"],
        label="Data de Nascimento",
        help_text = 'Formato : DD/MM/AAAA',
        widget=forms.DateInput(attrs={
            "placeholder":"DD/MM/AAAA"})
        )
    
