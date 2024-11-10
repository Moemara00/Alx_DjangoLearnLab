from django.urls import path
from . import views
urlpatterns = [
    path('',views.list_book, name = "list"),
    path("library/", views.details_library.as_view(), name = "library")

]