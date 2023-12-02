from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

# Create your models here.

# Vytvoříme si třídu s informacemi co chceme aby uvedl nový pojištěnec

class Pojistenec(models.Model):
    jmeno = models.CharField(max_length=100, verbose_name="Jméno")
    prijmeni = models.CharField(max_length=100, verbose_name="Příjmení")
    emial = models.EmailField(max_length=200, verbose_name="Email")
    telefon= models.CharField(max_length=20, verbose_name="Telefoní číslo")
    mesto = models.CharField(max_length=100, verbose_name="Město")
    ulice = models.CharField(max_length=100, verbose_name="ulice")
    pcs = models.CharField(max_length=5, verbose_name="PSČ")
# metoda slouží k vypsání informací o pojištěnci
    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"
    

class UzivatelManager(BaseUserManager):
    # vytvoříme uživatele
    def create_user(self, email, password):
        print(self.model)
        if email and password:
            user = self.model(email=self.normalize_email(email))
            user.set_password(password)
            user.save()
            return user
        
    # vytvoříme admina
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.save()
        return user
    

class Uzivatel(AbstractBaseUser):

    email = models.EmailField(max_length=300, unique=True)
    jmeno = models.CharField(max_length=100, verbose_name="Jméno", default='')
    prijmeni = models.CharField(max_length=100, verbose_name="Příjmení", default='')
    mesto = models.CharField(max_length=100, verbose_name="Město", default='')
    ulice = models.CharField(max_length=100, verbose_name="Ulice", default='')
    cislo = models.CharField(max_length=10, verbose_name="Číslo domu", default='')
    psc = models.CharField(max_length=10, verbose_name="PSČ", default='')
    telefon = models.CharField(max_length=20, verbose_name="Telefon", default='')
    is_admin = models.BooleanField(default=False)

    pojistky = models.ManyToManyField('Pojistka', related_name='pojistky', blank=True)


    class Meta:
        verbose_name = "uživatel"
        verbose_name_plural = "uživatelé"

    objects = UzivatelManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return f"{self.email} - {self.jmeno} {self.prijmeni}"
    
    @property
    def is_staff(self):
        return self.is_admin
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True 
    
class Pojistka(models.Model):
    TYPY_POJISTENI = [
        ('nemovitost', 'Pojištění nemovitosti'),
        ('auto', 'Pojištění auta'),
        ('veci', 'Pojištění věcí'),
        ('cestovni', 'Cestovní pojištění'),
    ]

    typ_pojisteni = models.CharField(
        max_length=20,
        choices=TYPY_POJISTENI,
        default='nemovitost',
        verbose_name='Typ pojištění'
    )
    uzivatele = models.ManyToManyField('Uzivatel', related_name='uzivatele', blank=True)


    castka = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Částka pojistky', default=0.00)
    predmet_pojisteni = models.TextField(verbose_name='Předmět pojištění', default="")
    datum_od = models.DateField(verbose_name='Platnost od', default=timezone.now)
    datum_do = models.DateField(verbose_name='Platnost do', default=timezone.now)

    def __str__(self):
        return f'{self.typ_pojisteni} - {self.predmet_pojisteni}'

    def save(self, *args, **kwargs):
        # Automaticky nastavit datum_do pro cestovní pojištění na 7 dní od data_od
        if self.typ_pojisteni == 'cestovni' and not self.datum_do:
            self.datum_do = self.datum_od + timezone.timedelta(days=7)
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name = 'Pojištění'
        verbose_name_plural = 'Pojištění'