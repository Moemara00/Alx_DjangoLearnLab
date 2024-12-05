from django.urls import path
from . import views

urlpatterns = [

    path('books/',views.ListView.as_view(),name='book-list'),
    path('books/<int:pk>/',views.DeleteView.as_view(),name='book-detail'),
    path('books/create/',views.CreateView.as_view(),name='book-create'),
    path('books/<int:pk>/update',views.UpdateView.as_view(),name='book-update'),
    path('books/<int:pk>/delete',views.DeleteView.as_view(),name='book-delete')
]