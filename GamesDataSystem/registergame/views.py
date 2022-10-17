from django.db import connection
from django.shortcuts import render, redirect


from django.shortcuts import render
from django.views import View
from django.urls import reverse
from .forms import RegisterGameForm, AddPlatformForm, AddDeveloperForm, RegisterSalesForm, EditGameForm, EditPlatformForm
from .models import *

# import generic UpdateView
from django.views.generic.edit import UpdateView


# Create your views here.
class HomeView(View):
    template = 'index.html'

    def get(self, request):
        sales = Sales.objects.all()

        return render(request, self.template, {'sales': sales})


class RegisterGame(View):
    template ='registerGame.html'

    def get(self, request):
        form = RegisterGameForm()
        return render(request, self.template, {'form':form})

    def post(self, request):
        form = RegisterGameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('registergame:index'))
        return render(request, self.template, {'form':form})


class AddPlatform(View):
    template = 'addPlatform.html'

    def get(self, request):
        form = AddPlatformForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = AddPlatformForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('registergame:index'))
        return render(request, self.template, {'form': form})


class AddDeveloper(View):
    template = 'addDeveloper.html'

    def get(self, request):
        form = AddDeveloperForm
        return render(request,self.template,{'form':form})

    def post(self, request):
        form = AddDeveloperForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('registergame:index'))
        return render(request, self.template,{'form':form})


class RegisterSales(View):
    template = 'registerSales.html'

    def get(self, request):
        form = RegisterSalesForm
        return render(request,self.template,{'form':form})

    def post(self, request):
        form = RegisterSalesForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('registergame:index'))
        return render(request, self.template,{'form':form})


class UpdateGame(View):
    template = 'updateGame.html'

    def get(self, request, game_id):
        game = Game.objects.get(pk=int(game_id))
        form = EditGameForm(instance=game)
        return render(request, self.template, {'form': form})

    def post(self, request, game_id):
        game = Game.objects.get(pk=int(game_id))
        form = EditGameForm(request.POST or None, instance=game)
        if form.is_valid:
            form.save()
        return redirect(reverse('registergame:games_list'))


class GamesList(View):
    template = 'displayGames.html'

    def get(self, request):
        gameslist = Game.objects.all()
        return render(request, self.template, {'gameslist': gameslist})


class SalesList(View):
    template = 'index.html'

    def get(self, request):
        sales = Sales.objects.all()
        return render(request, self.template, {'sales': sales})


class DeleteGame(View):
    template = 'displayGames.html'

    def get(self, request, game_id):
        game = Game.objects.get(pk=int(game_id))
        game.delete()
        return redirect(reverse('registergame:games_list'))


class SortByNameAtoZ(View):
    template = 'displayGames.html'

    def get(self, request):
        gameslist = Game.objects.all().order_by('name')
        return render(request, self.template, {'gameslist': gameslist})


class SortByNameZtoA(View):
    template = 'displayGames.html'

    def get(self, request):
        gameslist = Game.objects.all().order_by('-name')
        return render(request, self.template, {'gameslist': gameslist})


class SortByYear(View):
    template = 'displayGames.html'

    def get(self, request):
        gameslist = Game.objects.all().order_by('year_released')
        return render(request, self.template, {'gameslist': gameslist})


class SortByPC(View):
    template = 'displayGames.html'

    def get(self, request):
        gameslist = Game.objects.filter(platform_id='PC').order_by('name')
        return render(request, self.template, {'gameslist': gameslist})


class SortByXB(View):
    template = 'displayGames.html'

    def get(self, request):
        gameslist = Game.objects.filter(platform_id='XB').order_by('name')
        return render(request, self.template, {'gameslist': gameslist})


class SortByPS(View):
    template = 'displayGames.html'

    def get(self, request):
        gameslist = Game.objects.filter(platform_id='PS').order_by('name')
        return render(request, self.template, {'gameslist': gameslist})


class DeletePlatform(View):
    template = 'displayPlatform.html'

    def get(self, request, platform_id):
        platform = Platform.objects.get(pk=str(platform_id))
        platform.delete()
        return redirect(reverse('registergame:platform_list'))


class PlatformList(View):
    template = 'displayPlatform.html'

    def get(self, request):
        platformlist = Platform.objects.all()
        return render(request, self.template,
        {'platformlist': platformlist})


class EditPlatform(View):
    template = 'editPlatform.html'

    def get(self, request, platform_id):
        platform = Platform.objects.get(pk=str(platform_id))
        form = EditPlatformForm(instance=platform)
        return render(request, self.template, {'form': form})

    def post(self, request, platform_id):
        platform = Platform.objects.get(pk=str(platform_id))
        form = EditPlatformForm(request.POST or None, instance=platform)
        if form.is_valid:
            form.save()
            platform.save(update_fields=['platform_developer'])
        return redirect(reverse('registergame:platform_list'))


class SalesSortByYearASC(View):
    template = 'index.html'

    def get(self, request):
        sales = Sales.objects.all().order_by('year')
        return render(request, self.template, {'sales':sales})


class SalesSortByYearDESC(View):
    template = 'index.html'

    def get(self, request):
        sales = Sales.objects.all().order_by('-year')
        return render(request, self.template, {'sales':sales})


class SalesASC(View):
    template = 'index.html'

    def get(self, request):
        sales = Sales.objects.all().order_by('sales')
        return render(request, self.template, {'sales':sales})


class SalesDESC(View):
    template = 'index.html'

    def get(self, request):
        sales = Sales.objects.all().order_by('-sales')
        return render(request, self.template, {'sales':sales})


class SalesAsia(View):
    template = 'index.html'

    def get(self, request):
        sales = Sales.objects.filter(region_id=1).order_by('sales')
        return render(request, self.template, {'sales': sales})


class SalesSA(View):
    template = 'index.html'

    def get(self, request):
        sales = Sales.objects.filter(region_id=2).order_by('sales')
        return render(request, self.template, {'sales': sales})


class SalesAntarctica(View):
    template = 'index.html'

    def get(self, request):
        sales = Sales.objects.filter(region_id=3).order_by('sales')
        return render(request, self.template, {'sales': sales})


class SalesNA(View):
    template = 'index.html'

    def get(self, request):
        sales = Sales.objects.filter(region_id=4).order_by('sales')
        return render(request, self.template, {'sales': sales})


class SalesEurope(View):
    template = 'index.html'

    def get(self, request):
        sales = Sales.objects.filter(region_id=5).order_by('sales')
        return render(request, self.template, {'sales': sales})


class SalesAfrica(View):
    template = 'index.html'

    def get(self, request):
        sales = Sales.objects.filter(region_id=6).order_by('sales')
        return render(request, self.template, {'sales': sales})


class SalesOceania(View):
    template = 'index.html'

    def get(self, request):
        sales = Sales.objects.filter(region_id=7).order_by('sales')
        return render(request, self.template, {'sales': sales})
