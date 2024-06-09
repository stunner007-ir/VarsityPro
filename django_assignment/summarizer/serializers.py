# summarization/serializers.py

from rest_framework import serializers


class SummarizeTextSerializer(serializers.Serializer):
    text = serializers.CharField()
