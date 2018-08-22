from django.test import TestCase
from .models import Mineral
from django.urls import reverse


# Create your tests here.
class ViewTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name='test',
            image_filename='test',
            image_caption='test',
            category='test',
            formula='test',
            strunz_classification='test',
            crystal_system='test1',
            unit_cell='test',
            color='test',
            crystal_symmetry='test',
            cleavage='test',
            mohs_scale_hardness='test',
            luster='test',
            streak='test',
            diaphaneity='test',
            optical_properties='test',
            refractive_index='test',
            crystal_habit='test',
            specific_gravity='test',
            group='test'
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

    def test_search_by_letter_view(self):
        resp = self.client.get(reverse('minerals:letter_search',
                                       kwargs={'letter': 't'}
                                       ))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')
        self.assertContains(resp, self.mineral.name)
        self.assertIn(self.mineral, resp.context['minerals'])

    def test_search_by_group_view(self):
        resp = self.client.get(reverse('minerals:group_search',
                                       kwargs={'group': 'test'}
                                       ))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')
        self.assertContains(resp, self.mineral.name)
        self.assertIn(self.mineral, resp.context['minerals'])
