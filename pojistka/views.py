# pojistka/views.py
from django.shortcuts import render, redirect
from django.views import View, generic
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from .forms import UzivatelForm, LoginForm, PojistkaForm
from .models import Uzivatel
from django.contrib import messages

class HomeView(TemplateView):
    template_name = "base.html"

class PridatPojistenceView(View):
    template_name = "pojistka/vytvor_pojistence_form.html"

    def get(self, request):
        form = UzivatelForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UzivatelForm(request.POST)
        if form.is_valid():
            uzivatel = form.save(commit=False)
            uzivatel.set_password(form.cleaned_data['password'])
            uzivatel.save()
            
            # Můžete přidat další logiku podle potřeby

            messages.success(request, 'Pojištěnec byl úspěšně vytvořen.')
            login(request, uzivatel)  # Automatické přihlášení po vytvoření účtu

            return redirect('seznam_pojistencu')
        else:
            messages.error(request, 'Omlouváme se, došlo k chybě při vytváření pojištěnce. Zkontrolujte formulář.')

        return render(request, self.template_name, {'form': form})


class SeznamUzivateluView(View):
    template_name = 'pojistka/seznam_pojistencu.html'

    def get(self, request, *args, **kwargs):
        uzivatele = Uzivatel.objects.all()
        return render(request, self.template_name, {'uzivatele': uzivatele})

class UzivatelDetailView(generic.DetailView):
    model = Uzivatel
    template_name = 'pojistka/uzivatel_detail.html'
    context_object_name = 'uzivatel'

    def get(self, request, pk):
        try:
            uzivatel = Uzivatel.objects.get(pk=pk)
        except:
            return redirect("seznam_pojistencu")
        return render(request, self.template_name, {"uzivatel": uzivatel})
    


class UzivatelViewRegister(generic.edit.CreateView):
    form_class = UzivatelForm
    model = Uzivatel
    template_name = "pojistka/user_form.html"

    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, "Už jsi přihlášený, nemůžeš se registrovat.")
            return redirect("home")
        else:
            form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        if request.user.is_authenticated:
            messages.info(request, "Už jsi přihlášený, nemůžeš se registrovat.")
            return redirect("home")  
        form = self.form_class(request.POST)
        if form.is_valid():
            uzivatel = form.save(commit=False)
            password = form.cleaned_data["password"]
            uzivatel.set_password(password)
            uzivatel.save()
            login(request, uzivatel)
            return redirect("home")
        return render(request, self.template_name, {"form": form})
    
class UzivatelViewLogin(generic.CreateView):
    form_class = LoginForm
    template_name = "pojistka/user_form.html"

    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, "Už jsi přihlášený, nemůžeš se přihlásit znovu.")
            return redirect("home")
        else:
            form = self.form_class(None)
        return render(request, self.template_name, {"form": form})
    
    def post(self, request):
        if request.user.is_authenticated:
            messages.info(request, "Už jsi přihlášený, nemůžeš se přihlásit znovu.")
            return redirect("home")
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Tento účet neexistuje.")
        return render(request, self.template_name, {"form": form})
        
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    else:
        messages.info(request, "Nemužeš se odhlásit, pokud nejsi přihlášený.")
    return redirect("login")

class VytvoritPojistkuView(View):
    template_name = "pojistka/vytvorit_pojistku.html"

    def get(self, request):
        form = PojistkaForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PojistkaForm(request.POST)
        if form.is_valid():
            pojistka = form.save(commit=False)  # Neprovádět uložení do databáze okamžitě
            pojistka.save()  # Uložit pojistku do databáze

            # Přidání aktuálního uživatele k pojistce
            request.user.pojistky.add(pojistka)

            return redirect('uzivatel_detail', pk=request.user.pk)  # Přesměrování na detail uživatele vytvořených pojistek
        else:
            # Zpracování chybného formuláře
            return render(request, self.template_name, {'form': form})
           