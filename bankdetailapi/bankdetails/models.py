from django.db import models
# Create your models here.


class BankDetails(models.Model):
    ifsc = models.CharField(max_length=11, blank=False, null=False, unique=True)
    bank_id = models.BigIntegerField(blank=False, null=False)
    branch = models.CharField(max_length=74, blank=False, null=False)
    address = models.CharField(max_length=195, blank=False, null=False)
    city = models.CharField(max_length=50, blank=False, null=False)
    district = models.CharField(max_length=50, blank=False, null=False)
    state = models.CharField(max_length=26, blank=False, null=False)
    bank_name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return str(self.ifsc)
