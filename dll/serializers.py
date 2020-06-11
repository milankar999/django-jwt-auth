from rest_framework import serializers
from .models import *
 
 
class DBSerializer(serializers.ModelSerializer):
 
    class Meta(object):
        model = DB
        fields = ('pp','po')