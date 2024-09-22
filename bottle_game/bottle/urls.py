from django.urls import path
from .views import CreateBottleView
urlpatterns = [
    path("creat-bottle/", CreateBottleView.as_view())
]