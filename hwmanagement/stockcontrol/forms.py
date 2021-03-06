import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.forms import inlineformset_factory

from .models import ProbeCardReport, ProbeCard

class ProbeCardReportForm(forms.ModelForm):
        
    class Meta:
        model = ProbeCardReport
        exclude = ('date_added', 'author')
        widgets = {'date_measured': forms.DateInput(attrs={'class': 'datepicker'}),
                   'iqa_date': forms.DateInput(attrs={'class': 'datepicker'}),
                  }
        
    def clean(self):
        cleaned_data = super(ProbeCardReportForm, self).clean()

        date_measured = cleaned_data.get('date_measured')
        iqa_date = cleaned_data.get('iqa_date')

        if date_measured > datetime.date.today():
            raise ValidationError(_('Date measured should not be in the future'))
        if date_measured < datetime.date(2012,1,1):
            raise ValidationError(_('Date measured is too far in the past'))
        if iqa_date > datetime.date.today():
            raise ValidationError(_('Iqa date should not be in the future'))
        if iqa_date < datetime.date(2012,1,1):
            raise ValidationError(_('Iqa date is too far in the past'))
        return cleaned_data
        

    def __init__(self, *args, **kwargs):
        #print(kwargs)
        #print(kwargs['initial']['author'])
        self.author = kwargs['initial']['author']
        super(ProbeCardReportForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super(ProbeCardReportForm, self).save(False)
        obj.author = self.author
        commit and obj.save()
        return obj

    
class SelectProbeCardModelForm(forms.ModelForm):
    
    class Meta:
        model = ProbeCardReport
        fields = ['probecard']
        labels = {'probecard': _('ProbeCard:')}
        help_texts = {'probecard': _('Select a probecard.')}        

        
class SelectBBKingPCModelForm(forms.ModelForm):

    class Meta:
        model = ProbeCardReport
        fields = ['probecard']
        labels = {'probecard': _('ProbeCard:')}
        help_texts = {'probecard': _('Select a BBKing Probecard,')}

    def __init__(self, *args, **kwargs):
        super(SelectBBKingPCModelForm, self).__init__(*args, **kwargs)
        self.fields['probecard'].queryset = ProbeCardReport.objects.filter(probecard__device_name__icontains='bb king')
        
        
class SelectMerlePCModelForm(forms.ModelForm):

    class Meta:
        model = ProbeCardReport
        fields = ['probecard']
        labels = {'probecard': _('ProbeCard:')}
        help_texts = {'probecard': _('Select a Merle Probecard,')}

    def __init__(self, *args, **kwargs):
        super(SelectMerlePCModelForm, self).__init__(*args, **kwargs)
        self.fields['probecard'].queryset = ProbeCardReport.objects.filter(probecard__device_name__icontains='merle')
        

class SelectJoeCPCModelForm(forms.ModelForm):

    class Meta:
        model = ProbeCardReport
        fields = ['probecard']
        labels = {'probecard': _('ProbeCard:')}
        help_texts = {'probecard': _('Select a JoeC Probecard,')}

    def __init__(self, *args, **kwargs):
        super(SelectJoeCPCModelForm, self).__init__(*args, **kwargs)
        self.fields['probecard'].queryset = ProbeCardReport.objects.filter(probecard__device_name__icontains='joec')


class SelectJoeCockerPCModelForm(forms.ModelForm):

    class Meta:
        model = ProbeCardReport
        fields = ['probecard']
        labels = {'probecard' : _('ProbeCard:')}
        help_texts = {'probecard': _('Select a Joe Crocker Probecard,')}

    def __init__(self, *args, **kwargs):
        super(SelectJoeCockerPCModelForm, self).__init__(*args, **kwargs)
        self.fields['probecard'].queryset = ProbeCardReport.objects.filter(probecard__device_name__icontains = 'joe cocker')


class SelectLesPaulPCModelForm(forms.ModelForm):

    class Meta:
        model = ProbeCardReport
        fields = ['probecard']
        labels = {'probecard' : _('ProbeCard:')}
        help_texts = {'probecard': _('Select a LesPaul Probecard,')}

    def __init__(self, *args, **kwargs):
        super(SelectLesPaulPCModelForm, self).__init__(*args, **kwargs)
        self.fields['probecard'].queryset = ProbeCardReport.objects.filter(probecard__device_name__icontains = 'lespaul')
        

class SelectJaniPCModelForm(forms.ModelForm):

    class Meta:
        model = ProbeCardReport
        fields = ['probecard']
        labels = {'probecard' : _('ProbeCard:')}
        help_texts = {'probecard': _('Select a Jani Probecard,')}

    def __init__(self, *args, **kwargs):
        super(SelectJaniPCModelForm, self).__init__(*args, **kwargs)
        self.fields['probecard'].queryset = ProbeCardReport.objects.filter(probecard__device_name__icontains = 'jani')
        

class SelectWomackPCModelForm(forms.ModelForm):

    class Meta:
        model = ProbeCardReport
        fields = ['probecard']
        labels = {'probecard' : _('ProbeCard:')}
        help_texts = {'probecard': _('Select a Womack Probecard,')}

    def __init__(self, *args, **kwargs):
        super(SelectWomackPCModelForm, self).__init__(*args, **kwargs)
        self.fields['probecard'].queryset = ProbeCardReport.objects.filter(probecard__device_name__icontains = 'womack')



class PCInstanceForm(forms.ModelForm):
   
    class Meta:
        model = ProbeCardReport
        exclude =  ('probecard','probehead_rebuild_num','date_added','author')
        widgets = {'date_measured': forms.DateInput(attrs={'class': 'datepicker'}),
                   'iqa_date': forms.DateInput(attrs={'class': 'datepicker'}),
                  }
                  
    def clean(self):
        cleaned_data = super(PCInstanceForm, self).clean()

        date_measured = cleaned_data.get('date_measured')
        iqa_date = cleaned_data.get('iqa_date')

        if date_measured > datetime.date.today():
            raise ValidationError(_('Date should not be in the future'))
        if date_measured < datetime.date(2012,1,1):
            raise ValidationError(_('Date is too far in the past'))
        if iqa_date > datetime.date.today():
            raise ValidationError(_('Date should not be in the future'))
        if iqa_date < datetime.date(2012,1,1):
            raise ValidationError(_('Date is too far in the past'))
        return cleaned_data    

    def __init__(self, *args, **kwargs):
        self.author = kwargs['initial']['author']
        super(PCInstanceForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super(PCInstanceForm, self).save(False)
        obj.author = self.author
        commit and obj.save()
        return obj
