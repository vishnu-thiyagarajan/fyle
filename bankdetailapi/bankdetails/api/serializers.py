from rest_framework import serializers
from bankdetails.models import BankDetails


class ActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankDetails
        fields = ['pk', 'ifsc', 'bank_id', 'branch', 'address', 'city', 'district', 'state', 'bank_name']
