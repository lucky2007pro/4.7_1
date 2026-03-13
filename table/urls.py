from django.urls import path
from .views import table, plus1
urlpatterns = [
    path('table/', table),
    path('plus1/', plus1),
]