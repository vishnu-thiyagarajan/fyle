# Create your views here.
from rest_framework import generics
from bankdetails.models import BankDetails
from .serializers import ActionSerializer
from rest_framework.permissions import IsAuthenticated


class GetBankDetails(generics.ListAPIView):
    lookup_feild = ('ifsc', 'bank_name', 'city')
    permission_classes = (IsAuthenticated,)
    serializer_class = ActionSerializer

    def get_queryset(self):
        ifsc =  self.request.query_params.get("ifsc", None)
        bank_name = self.request.query_params.get("name", None)
        city = self.request.query_params.get("city", None)
        val = None
        if ifsc:
            val = BankDetails.objects.filter(ifsc=ifsc)
        if bank_name and city:
            val = BankDetails.objects.filter(bank_name=bank_name, city=city)
        return val
