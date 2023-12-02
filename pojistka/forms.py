# forms.py
from django import forms
from .models import Pojistenec, Uzivatel, Pojistka
from django.core.exceptions import ValidationError



# vytvoříme si formulář pro přidání pojištence
class PojistenecForm(forms.ModelForm):
    class Meta:
        model = Pojistenec
        fields = '__all__'


    class Meta:
        model = Pojistenec
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        jmeno = cleaned_data.get('jmeno')
        prijmeni = cleaned_data.get('prijmeni')

        # Příklad: Zkontrolovat, zda jméno a příjmení neobsahují čísla
        if any(char.isdigit() for char in jmeno):
            self.add_error('jmeno', 'Jméno nemůže obsahovat čísla.')

        if any(char.isdigit() for char in prijmeni):
            self.add_error('prijmeni', 'Příjmení nemůže obsahovat čísla.')


class UzivatelForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    jmeno = forms.CharField(max_length=100, label='Jméno')
    prijmeni = forms.CharField(max_length=100, label='Příjmení')
    telefon = forms.CharField(max_length=20, label='Telefonní číslo')
    mesto = forms.CharField(max_length=100, label='Město')
    ulice = forms.CharField(max_length=100, label='Ulice')
    cislo = forms.CharField(max_length=10, label='č. domu')
    psc = forms.CharField(max_length=10, label='PSČ')

    class Meta:
        model = Uzivatel
        fields = ['email', 'password', 'jmeno', 'prijmeni', 'telefon', 'mesto', 'ulice', 'cislo', 'psc']

        def clean_email(self):
            email = self.cleaned_data['email']
            if '@' not in email:
                raise ValidationError('E-mail musí obsahovat znak @.')
            return email

        def clean_jmeno(self):
            jmeno = self.cleaned_data['jmeno']
            if any(char.isdigit() for char in jmeno):
                raise ValidationError('Jméno nesmí obsahovat číslo.')
            return jmeno

        def clean_prijmeni(self):
            prijmeni = self.cleaned_data['prijmeni']
            if any(char.isdigit() for char in prijmeni):
                raise ValidationError('Příjmení nesmí obsahovat číslo.')
            return prijmeni

class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ["email", "password"]   

class PojistkaForm(forms.ModelForm):
    # Definujte pole pro výběr typu pojištění
    TYPY_POJISTENI = [
        ('nemovitost', 'Pojištění nemovitosti'),
        ('auto', 'Pojištění auta'),
        ('veci', 'Pojištění věcí'),
        ('cestovni', 'Cestovní pojištění'),
    ]

    typ_pojisteni = forms.ChoiceField(
        choices=TYPY_POJISTENI,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Typ pojištění'
    )

    class Meta:
        model = Pojistka
        fields = ['typ_pojisteni', 'castka', 'predmet_pojisteni', 'datum_od', 'datum_do']