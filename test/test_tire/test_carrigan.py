import unittest
from tire.carrigan_tire import CarriganTire

class TestCarrigan(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.9, 1.2, 0.4, 0.9]
        tire = CarriganTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.3, 0.6, 0.1, 0.4]
        tire = CarriganTire(tire_wear)
        self.assertFalse(tire.needs_service())
        