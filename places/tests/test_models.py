from django.test import TestCase
from model_mommy import mommy

from places.models import Region, Municipality


class MunicipalityTestCase(TestCase):
    def setUp(self):
        self.regions = mommy.make(Region, 2)
        self.municipality = mommy.make(Municipality, is_active=True)

    def test_save(self):
        for region in self.regions:
            region.municipalities.add(self.municipality)

        self.assertEqual(self.regions[0].municipalities.count(), 1)

        self.municipality.is_active = False
        self.municipality.save(update_fields=['is_active'])

        self.assertEqual(self.regions[0].municipalities.count(), 0)
