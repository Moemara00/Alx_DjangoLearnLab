from rest_framework import serializers
from datetime import datatime
def validate_publication_year(self,value):
    current_year = datatime.now().year

    if value > current_year:
        raise serializers.ValidationError("Sorry this is  a future date !")
    