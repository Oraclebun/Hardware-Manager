from django.db import models
from django.urls import reverse #Used to generate URLs by reversing URLs patterns
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class ProbeCard(models.Model):
    """Model represening a ProbeCard (but not a specific copy of the card)."""
    probecard_id = models.CharField(max_length=30)
    device_num = models.CharField(max_length=30)
    device_name = models.CharField(max_length=20, help_text = 'Enter device group name (e.g. Merle)')
    aus_serial_num = models.CharField(max_length=30, help_text = 'Enter probecard serial number') #Austin PC Serial Num

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.probecard_id}-({self.device_name})'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this probecard."""
        return reverse('probecard-detail', args=[str(self.id)])

    
class ProbeCardReport(models.Model):
    """Model representing a specific report of a probecard."""
    probecard = models.ForeignKey('ProbeCard', on_delete = models.CASCADE)
    probehead_rebuild_num = models.IntegerField(null = False, blank = False, default = 0)
    probehead_num = models.CharField(max_length=20, help_text = 'Probehead serial number')
    date_measured = models.DateField(null = True, blank = True, help_text = 'Enter date in YYYY-MM-DD format')
    tip_length = models.DecimalField(max_digits = 4, decimal_places=1, null = True, blank = True, help_text = 'Enter tip lenght in 1 dec place')
    crown_height = models.DecimalField(max_digits= 4, decimal_places=1, null = True, blank = True, help_text = 'Enter crown height in 1 dec place')
    probehead_touchdown = models.IntegerField(null = True, blank = True)
    pcb_touchdown = models.IntegerField(null = True,blank = True)
    iqa_date = models.DateField(null=True, blank = True, help_text = 'Enter date in YYYY-MM-DD format')
    iqa_tip_length = models.DecimalField(max_digits = 4, decimal_places=1, null = True, blank =True)
    crown_iqa_height = models.DecimalField(max_digits = 4, decimal_places=1, null = True, blank = True)
    remarks= models.CharField(max_length = 50, blank = True)
    date_added = models.DateField(default = date.today())
    author = models.ForeignKey(User, on_delete = models.PROTECT, blank = False, null = True)

    LOG_STATUS = (
        ('r', 'Rebuilt'),
        ('a', 'Active'),
        ('o', 'Obsolete'),
        ('b', 'Shipped Back'),
        ('s', 'Swap PH'),
        ('d', 'Damaged'),
        )

    status_log = models.CharField(
        max_length=1,
        choices = LOG_STATUS,
        blank = True,
        default = '',
        help_text = 'Status base on Remarks',
        )

    PC_FUNC_STATUS = (
        ('g', 'Good'),
        ('b', 'Bad'),
        )
    status_pc = models.CharField(
        max_length = 1,
        choices = PC_FUNC_STATUS,
        blank = True,
        default = '',
        help_text = 'ProbeCard Status',
        )
    PROD_STATUS = (
        ('y', 'Yes'),
        ('n', 'No'),
        )
    status_prod = models.CharField(
        max_length = 1,
        choices = PROD_STATUS,
        blank = True,
        default = '',
        help_text = 'In Production?',
        )
    
    class Meta:
        ordering = ['probecard', 'probehead_rebuild_num']
        permissions = (("can_edit_status", "Edit ProbeCard status"),)
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.probecard.probecard_id}/{self.probehead_rebuild_num}'

    def get_absolute_url(self):
        """Returns the url to access a particular probecard report instance."""
        return reverse('pcreport-detail', args=[str(self.id)])
