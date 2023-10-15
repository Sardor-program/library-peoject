from rest_framework import serializers
from rest_framework.exceptions import ValidationError


from .models import Book


class BookSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Book
        fields = ('id', 'title', 'content', 'subtitle', 'author', 'isbn', 'price')


