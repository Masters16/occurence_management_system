from django import forms

from . import models


class OccurenceRecordsForm(forms.ModelForm):
    class Meta:
        model = models.OccurenceRecords
        fields = ['record_id', 'police', 'station_id','user_id', 'description', 'address','status','created_date']
