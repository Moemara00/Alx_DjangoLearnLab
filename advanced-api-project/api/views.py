from rest_framework import generics
from datetime import datetime
from .models import Book
from .serializers import BookSerializer
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters 
from .models import Author


class ListView(generics.ListAPIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ('title','author__name')

    def get_queryset(self):
        
        author = Author.objects.all().order_by("?").first()
        qs = Book.objects.filter(author=author)
        
        return qs
        


class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        current_year = datetime.now().year
        if serializer.publication_year > current_year:
            raise serializers.ValidationError("Sorry This year is in the future")

        return super().perform_create(serializer)

class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    def perform_update(self, serializer):
        current_year = datetime.now().year
        if serializer.publication_year > current_year:
            raise serializers.ValidationError("Sorry This year is in the future")
        return super().perform_update(serializer)

class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]