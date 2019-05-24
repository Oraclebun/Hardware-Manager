from django.test import TestCase

from stockcontrol.models import ProbeCard, ProbeCardReport
from .test_base import TestData
# Create your tests here.

class ProbeCardModelTest(TestData):
#Set up non-modified objects used by all test methods

    @classmethod
    def setUpTestData(cls):
        cls.probecard = cls._create_pc()
        
    def test_probecard_id_label(self):
        probecard = self.probecard
        field_label = probecard._meta.get_field('probecard_id').verbose_name
        self.assertEquals(field_label, 'probecard id')

    def test_device_num_label(self):
        probecard = self.probecard
        field_label = probecard._meta.get_field('device_num').verbose_name
        self.assertEquals(field_label, 'device num')

    def test_device_name_label(self):
        probecard = self.probecard
        field_label = probecard._meta.get_field('device_name').verbose_name
        self.assertEquals(field_label, 'device name')

    def test_aus_serial_num_label(self):
        probecard = self.probecard
        field_label = probecard._meta.get_field('aus_serial_num').verbose_name
        self.assertEquals(field_label, 'aus serial num')

    def test_probecard_id_max_length(self):
        probecard = self.probecard
        max_length = probecard._meta.get_field('probecard_id').max_length
        self.assertEquals(max_length, 30)

    def test_device_num_max_length(self):
        probecard = self.probecard
        max_length = probecard._meta.get_field('device_num').max_length
        self.assertEquals(max_length, 30)

    def test_device_name_max_length(self):
        probecard = self.probecard
        max_length = probecard._meta.get_field('device_name').max_length
        self.assertEquals(max_length, 20)

    def test_aus_serial_num_max_length(self):
        probecard = self.probecard
        max_length = probecard._meta.get_field('aus_serial_num').max_length
        self.assertEquals(max_length, 30)

    def test_object_name_is_probecard_id_dash_device_name(self):
        probecard = self.probecard
        expected_object_name = f'{probecard.probecard_id}-({probecard.device_name})'
        self.assertEquals(expected_object_name, str(probecard))

    def test_probecard_get_absolute_url(self):
        probecard = self.probecard
        self.assertEquals(probecard.get_absolute_url(), '/stockcontrol/allpc/4')


class ProbeCardReportModelTest(TestData):
        #Set up non-modified objects used by all test methods
        
    def test_object_name_is_probecard_id_slash_probehead_rebuild_num(self):
        probecard = self._create_pc()
        pcreport = self._create_pcinstance1()
        expected_object_name = f'{pcreport.probecard.probecard_id}/{pcreport.probehead_rebuild_num}'
        self.assertEquals(expected_object_name, str(pcreport))

    def test_pcreport_get_absolute_url(self):
        pcreport = self._create_pcinstance1()
        self.assertEquals(pcreport.get_absolute_url(), '/stockcontrol/probecardreport/edit_report/3')

