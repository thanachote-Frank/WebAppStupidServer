from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from hadoop.models import Job


class JobSerializer(ModelSerializer):

    class Meta:
        model = Job
        fields = ('id', 'input', 'result')


class RequestSerializer(serializers.Serializer):
    jobId = serializers.IntegerField(min_value=0)