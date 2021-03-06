from django.test import TestCase
from django.urls import reverse

from stockcontrol.models import ProbeCard, ProbeCardReport
# Create your tests here.

class ProbeCardListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_probecard = 20

        for pc_id in range(number_of_probecard):
            ProbeCard.objects.create(
                probecard_id=f'IF/U-1234567 {pc_id}',
                device_name=f'Rocker {pc_id}',
            )


    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/stockcontrol/allpcs/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('allpcs'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('allpcs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stockcontrol/probecard_list.html')
