from rest_framework import serializers
from .models import JobList

class JobListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'published',
            'time_in_work',
            'status',
            'manager',
            'executor',
            'price',
            'name',
            'surname',
            'patronymic',
            'phone',
            'email',
            'address',
            'comment',
            'appearance',
            'device',
            'imei_sn',
            'brand',
            'model',
            'equipment',
            'password',
            'estimated_price',
        )
        model = JobList