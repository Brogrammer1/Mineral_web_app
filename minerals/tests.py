from django.test import TestCase
from .models import Mineral
from django.urls import reverse

# Create your tests here.
class ViewTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name='test1',
            image_filename='test1',
            image_caption='test1',
            category='test1',
            formula='test1',
            strunz_classification='test1',
            crystal_system='test1',
            unit_cell='test1',
            color='test1',
            crystal_symmetry='test1',
            cleavage='test1',
            mohs_scale_hardness='test1',
            luster='test1',
            streak='test1',
            diaphaneity='test1',
            optical_properties='test1',
            refractive_index='test1',
            crystal_habit='test1',
            specific_gravity='test1',
            group='test1'
        )


    def test_home_view(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')
        self.assertContains(resp, self.mineral.name)
        self.assertIn(self.mineral, resp.context['minerals'])

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.mineral.name)
        self.assertTemplateUsed(resp, 'mineral_detail.html')


    def test_random_view(self):
        resp = self.client.get(reverse('minerals:random'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'mineral_detail.html')





