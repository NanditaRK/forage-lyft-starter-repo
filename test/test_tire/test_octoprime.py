import unittest
from tire.octoprime_tire import OctoprimeTire


class TestOctoprime(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.9, 0.8, 0.7, 0.7]
        tire = OctoprimeTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.3, 0.1, 0.1, 0.2]
        tire = OctoprimeTire(tire_wear)
        self.assertFalse(tire.needs_service())
        