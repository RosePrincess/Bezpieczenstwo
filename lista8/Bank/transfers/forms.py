from django import forms
from .models import PreparedTransfer


class TransferForm(forms.ModelForm):
    def save(self, sender, commit=True):
        instance = super(forms.ModelForm, self).save(commit=False)
        instance.sender = sender

        if commit:
            instance.save()
            self.save_m2m()

        return instance

    class Meta:
        model = PreparedTransfer
        fields = [
            'receiver_name',
            'receiver_account',
            'title',
            'amount',
            'date'
        ]