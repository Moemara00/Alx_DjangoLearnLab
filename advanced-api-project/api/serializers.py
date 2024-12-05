from rest_framework import serializers
from .models import Book, Author
from rest_framework import validators
from datetime import datatime
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model= Book
        fields = [
            'title',
            'publication_year',
            'author',
        ]

    
    def validate_publication_year(self,value):
        current_year = datatime.now().year

        if value > current_year:
         raise serializers.ValidationError("Sorry this is  a future date !")
    

    publication_year = serializers.IntegerField(validators= [validate_publication_year])

class AuthorSerializer(serializers.ModelSerializer):
    author_books = serializers.SerializerMethodField(many=True,read_only=True)
    class Meta:
        model = Author
        fields = [
            'name',
            'author_books',
        ]

    def get_author_books(self,obj):

        return Book.objects.filter(author=obj.name)
    

