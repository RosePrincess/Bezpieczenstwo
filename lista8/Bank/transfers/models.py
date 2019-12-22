from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils import timezone

class PreparedTransfer(models.Model):
    account_regex = RegexValidator(regex=r'[0-9]{26}', message="Bank account must have 26 digits.")

    sender = models.ForeignKey(User, editable=False, null=False, on_delete=models.PROTECT)
    receiver_name = models.CharField(null=False, blank=False, max_length=50)
    receiver_account= models.CharField(validators=[account_regex], null=False, max_length=26)
    title = models.CharField(null=False, blank=False, max_length=100)
    amount = models.DecimalField(null=False, decimal_places=2, max_digits=10)
    date = models.DateTimeField(default=timezone.now)

class Transfer(models.Model):
    sender = models.ForeignKey(User,editable=False, null=False,  on_delete=models.PROTECT)
    receiver_name = models.CharField(null=False, blank=False, max_length=50)
    receiver_account = models.CharField(null=False, max_length=26)
    title = models.CharField(null=False, blank=False, max_length=100)
    amount = models.DecimalField(null=False, decimal_places=2, max_digits=10)
    date = models.DateTimeField(default=timezone.now)
    confirm = models.BooleanField(default=False)

