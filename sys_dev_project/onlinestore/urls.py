from django.urls import path
from . import views


urlpatterns = [
    path("store/items/", views.items),
    path("store/items/<int:item_id>/", views.items_one),
    

    
]