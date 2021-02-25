from rest_framework import serializers
from .models import ticket

class ticket_serializer(serializers.ModelSerializer):
    class Meta:
        model = ticket
        #exclude = ('id', 'title', 'description', 'completed')
        #depth = 3
        fields = '__all__'

