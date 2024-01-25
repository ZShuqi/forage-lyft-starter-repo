import unittest

from tires.octoprime_tires import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        sensors = [0.8, 0.8, 0.8, 0.7]
        tires = OctoprimeTires(sensors)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        sensors = [0.1, 0.2, 0.4, 0.2]
        tires = OctoprimeTires(sensors)
        self.assertFalse(tires.needs_service())
