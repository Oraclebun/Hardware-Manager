from django.test import TestCase

from stockcontrol.models import ProbeCard, ProbeCardReport
from django.contrib.auth.models import User
from datetime import date

class TestData(TestCase):

    def setUp(self):
        super().setUp()
        
    @classmethod
    def _create_pc(cls):
        test_probecard = ProbeCard.objects.create(probecard_id = 'IF/U-CS123Z987BMPX24/999', device_num = 'CS909L001-SX', device_name = 'Bon_Jovi', aus_serial_num = 'ZA909L100-ABC-90M00A-TG9')

        return test_probecard

    @classmethod
    def _get_pc(cls):
        test_pc = ProbeCard.objects.get(id=1)

        return test_pc

    @classmethod
    def _create_user(cls):
        test_user = User.objects.create_user(username = 'testuser1', email = 'test@test.com', password = 'top_secret')
        return test_user

    @classmethod
    def _create_user2(cls):
        test_user2 = User.objects.create_user(username = 'testuser2')
        return test_user2
    
    @classmethod
    def _create_pcinstance1(cls):
        probecard = cls._create_pc()
        test_user1 = cls._create_user()
        test_instance = ProbeCardReport.objects.create(probecard = probecard, probehead_rebuild_num= 99, probehead_num = 'AB1234567890-99', date_measured = '2017-05-08', tip_length = 99.99, crown_height = 99.99, probehead_touchdown = 9999999, pcb_touchdown = 9999999, iqa_date = '2017-05-08', iqa_tip_length = 99.99, crown_iqa_height = 99.99, author = test_user1, remarks = 'Rebuild to #9999', date_added = date.today(), status_log = 'r')

        return test_instance

