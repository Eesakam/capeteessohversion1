from django.urls import path
from Capeteesstock import views
from .views import SearchItem

app_name = "Capeteesstock"

urlpatterns = [
path("additem/",views.AddItem,name="additem"),
path("SOH/",views.SOH,name="SOH"),
path('search/',views.SearchItem, name="search"),
path("update_items/<str:pk>/",views.update_stock,name = "update_items"),
path("sale/<str:pk>/",views.sale,name = "sale"),
path("incoming/<str:pk>/",views.incoming,name = "incoming"),
]
