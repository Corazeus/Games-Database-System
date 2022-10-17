from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.urls import path

app_name = 'registergame'

urlpatterns =[
    path('', views.HomeView.as_view(), name='index'), #main page
    path('registerGame', views.RegisterGame.as_view(), name='register_game'),
    path('addPlatform', views.AddPlatform.as_view(), name='add_platform'),
    path('addDeveloper', views.AddDeveloper.as_view(), name='add_developer'),
    path('registerSales', views.RegisterSales.as_view(), name='register_sales'),
    path('gameslist', views.GamesList.as_view(), name='games_list'),
    path('saleslist', views.SalesList.as_view(), name='sales_list'),
    path('editGame/<int:game_id>', views.UpdateGame.as_view(), name='update_game'),
    path('deleteGame/<int:game_id>', views.DeleteGame.as_view(), name='delete_game'),
    #SORT GAMES
    path('gameslistAtoZ', views.SortByNameAtoZ.as_view(), name='games_list_AtoZ'),
    path('gameslistZtoA', views.SortByNameZtoA.as_view(), name='games_list_ZtoA'),
    path('sortByYear', views.SortByYear.as_view(), name='games_list_year'),
    path('sortByPC', views.SortByPC.as_view(), name='games_list_PC'),
    path('sortByXB', views.SortByXB.as_view(), name='games_list_XB'),
    path('sortByPS', views.SortByPS.as_view(), name='games_list_PS'),
    path('editPlatform/<str:platform_id>', views.EditPlatform.as_view(), name='edit_platform'),
    path('deletePlatform/<str:platform_id>', views.DeletePlatform.as_view(), name='delete_platform'),
    path('platformlist', views.PlatformList.as_view(), name='platform_list'),
    #SORT SALES
    path('salesByYearASC', views.SalesSortByYearASC.as_view(), name='sales_by_year_ASC'),
    path('salesByYearDESC', views.SalesSortByYearDESC.as_view(), name='sales_by_year_DESC'),
    path('salesASC', views.SalesASC.as_view(), name='sales_ASC'),
    path('salesDESC', views.SalesDESC.as_view(), name='sales_DESC'),
    path('salesAsia', views.SalesAsia.as_view(), name='sales_asia'),
    path('salesSA', views.SalesSA.as_view(), name='sales_SA'),
    path('salesAntarctica', views.SalesAntarctica.as_view(), name='sales_antarctica'),
    path('salesNA', views.SalesNA.as_view(), name='sales_NA'),
    path('salesEurope', views.SalesEurope.as_view(), name='sales_europe'),
    path('salesAfrica', views.SalesAfrica.as_view(), name='sales_africa'),
    path('salesOceania', views.SalesOceania.as_view(), name='sales_oceania'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)