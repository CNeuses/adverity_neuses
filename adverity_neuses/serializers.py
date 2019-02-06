from rest_framework import serializers

class Task1Serializer(serializers.Serializer):
   """Your data serializer, define your fields here."""
   comments = serializers.IntegerField()
   likes = serializers.IntegerField()


class Task2Serializer(serializers.Serializer):
   """Your data serializer, define your fields here."""
   comments = serializers.IntegerField()
   likes = serializers.IntegerField()