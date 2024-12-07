from rest_framework import serializers
from .models import Book, Author
from rest_framework import validators 
from datetime import date
# from .validators import validate_publication_year
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model= Book
        fields = [
            'title',
            'publication_year',
            'author',
        ]
    # publication_year = serializers.IntegerField(validators=[validate_publication_year])

    
    def validate_publication_year(self,value):
        current_year = 2024
        if value > current_year:
            print(current_year)
            raise serializers.ValidationError("Sorry this is  a future date !")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    author_books = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Author
        fields = [
            'name',
            'author_books',
        ]

    def get_author_books(self,obj):

        return Book.objects.filter(author=obj.name)
    

