from rest_framework import serializers

from .models import Quark

# Make your happy little serializers here
class QuarkSerializer(serializers.ModelSerializer):
    magic = serializers.SerializerMethodField()

    class Meta:
        model = Quark
        fields = ('mystery', 'name', 'magic', 'magic2')

    def get_magic(self, obj):
        return 'such magic'
