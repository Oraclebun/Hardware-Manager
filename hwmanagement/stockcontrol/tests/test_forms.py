import datetime

from django.test import TestCase
#from django.utils import timezone

from stockcontrol.forms import ProbeCardReportForm, PCInstanceForm
from stockcontrol.models import ProbeCard, ProbeCardReport
from django.contrib.auth.models import User
from .test_base import TestData
from django.urls import reverse
# Create your tests here.

class ProbeCardReportFormTest(TestData):
    @classmethod
    def setUpTestData(cls):
        cls.probecard = cls._create_pc()
        cls.user = cls._create_user()
        
    def test_create_form_date_field_help_text(self):
        user1 = self.user
        form = ProbeCardReportForm(initial = {'author':user1})
        self.assertEqual(form.fields['date_measured'].help_text, 'Enter date in YYYY-MM-DD format')

    def test_form_measured_date_in_past(self):
        pc = self.probecard
        user1 = self.user
        date = datetime.date(2011,12,31)
        form = ProbeCardReportForm(data = {
            'probecard' : pc.pk,
            'probehead_rebuild_num' : 99,
            'probehead_num' : 'ABC123',
            'date_measured' : date,
            'tip_length' : 99.9,
            'crown_height': 99.9,
            'probehead_touchdown' : 999,
            'pcb_touchdown' : 999,
            'iqa_date' : date,
            'iqa_tip_length' : 99.9,
            'crown_iqa_height' : 99.9,
        },initial = {'author': user1})
        self.assertFalse(form.is_valid())

    def test_form_measured_date_in_future(self):
        pc = self.probecard
        user1 = self.user
        date = datetime.date.today() + datetime.timedelta(days=1)
        form = ProbeCardReportForm(data = {
            'probecard' : pc.pk,
            'probehead_rebuild_num' : 99,
            'probehead_num' : 'TWINKLE234',
            'date_measured' : date,
            'iqa_date' : date,
            },initial = {'author': user1})
        self.assertFalse(form.is_valid())

    def test_form_measured_date_today(self):
        pc = self.probecard
        user1 = self.user
        date = datetime.date.today()
        form = ProbeCardReportForm(data = {
            'probecard' : pc.pk,
            'probehead_rebuild_num' : 999,
            'probehead_num' : 'MLK-0987',
            'date_measured' : date,
            'iqa_date' : date,
            }, initial = {'author': user1})
        self.assertTrue(form.is_valid())

class PCInstanceFormTest(TestData):
    @classmethod
    def setUpTestData(cls):
        cls.probecard = cls._create_pc()
        cls.pcrecord = cls._create_pcinstance1()
        cls.user2 = cls._create_user2()
        
    def test_create_form_date_field_help_text(self):
        pcrecord = self.pcrecord
        user1 = pcrecord.author
        form = PCInstanceForm(initial = {
            'author': user1,}
            )
        self.assertEqual(form.fields['date_measured'].help_text, 'Enter date in YYYY-MM-DD format')

    def test_form_measured_date_in_past(self):
        pc = self.probecard
        pcrecord = self.pcrecord
        date = datetime.date(2011,12,31)
        form = PCInstanceForm(initial = {
            'probecard' : pc.pk,
            'probehead_rebuild_num' : pcrecord.probehead_rebuild_num,
            'probehead_num' : pcrecord.probehead_num,
            'date_measured' : pcrecord.date_measured,
            'tip_length' : pcrecord.tip_length,
            'crown_height': pcrecord.crown_height,
            'probehead_touchdown' : pcrecord.probehead_touchdown,
            'pcb_touchdown' : pcrecord.pcb_touchdown,
            'iqa_date' : pcrecord.iqa_date,
            'iqa_tip_length' : pcrecord.iqa_tip_length,
            'crown_iqa_height' : pcrecord.crown_iqa_height,
            'author' : pcrecord.author,
            'remarks' : pcrecord.remarks,
            'status_log': pcrecord.status_log,
        }, data = {
            'date_measured' : date,
            'iqa_date' : date,
        })
        self.assertFalse(form.is_valid())

    def test_form_measured_date_in_future(self):
        pc = self.probecard
        pcrecord = self.pcrecord
        date = datetime.date.today() + datetime.timedelta(days=1)
        form = PCInstanceForm(initial = {
            'probecard' : pc.pk,
            'probehead_rebuild_num' : pcrecord.probehead_rebuild_num,
            'probehead_num' : pcrecord.probehead_num,
            'date_measured' : pcrecord.date_measured,
            'tip_length' : pcrecord.tip_length,
            'crown_height': pcrecord.crown_height,
            'probehead_touchdown' : pcrecord.probehead_touchdown,
            'pcb_touchdown' : pcrecord.pcb_touchdown,
            'iqa_date' : pcrecord.iqa_date,
            'iqa_tip_length' : pcrecord.iqa_tip_length,
            'crown_iqa_height' : pcrecord.crown_iqa_height,
            'author' : pcrecord.author,
            'remarks' : pcrecord.remarks,
            'status_log': pcrecord.status_log,
        }, data = {
            'date_measured' : date,
            'iqa_date' : date,
        })
        self.assertFalse(form.is_valid())

    def test_form_measured_date_today(self):
        pc = self.probecard
        pcrecord = self.pcrecord
        user2 = self.user2
        date = datetime.date.today()

        response = self.client.post(
            reverse('pcreport-detail',args=(pc.pk,)),
            {'date_measured' : date, 'iqa_date': date})
        
        self.assertEqual(response.status_code,302)

        form = PCInstanceForm(initial={
            'probecard' : pc.pk,
            'author' : pcrecord.author,
            }, data = {
                'date_measured' : date,
                'iqa_date' : date,
                'author' : user2,
            })


    

