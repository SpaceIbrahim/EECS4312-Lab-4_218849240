import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from dispense import DispenseEvent


class TestDispensingSubsystem(unittest.TestCase):

    def test_valid_event_passes_invariant(self):
        existing = []
        e = DispenseEvent("p1", "medA", 10, 5)  # total = 50 < 200
        self.assertTrue(DispenseEvent.invariant_holds(existing, e))

    def test_constructor_rejects_invalid_dose(self):
        with self.assertRaises(ValueError):
            DispenseEvent("p1", "medA", 0, 1)   # dose must be > 0
        with self.assertRaises(ValueError):
            DispenseEvent("p1", "medA", -5, 1)  # dose must be > 0

    def test_constructor_rejects_invalid_quantity(self):
        with self.assertRaises(ValueError):
            DispenseEvent("p1", "medA", 10, 0)   # quantity must be > 0
        with self.assertRaises(ValueError):
            DispenseEvent("p1", "medA", 10, -2)  # quantity must be > 0
        with self.assertRaises(ValueError):
            DispenseEvent("p1", "medA", 10, 1.5) # quantity must be int

    def test_invariant_blocks_duplicate_patient_medication(self):
        existing = [DispenseEvent("p1", "medA", 10, 1)]
        new_event = DispenseEvent("p1", "medA", 20, 1)  # same patient + same medication
        self.assertFalse(DispenseEvent.invariant_holds(existing, new_event))

    def test_invariant_blocks_exceeding_max_daily_dose(self):
        existing = []
        too_much = DispenseEvent("p1", "medA", 50, 5)  # total = 250 > 200
        self.assertFalse(DispenseEvent.invariant_holds(existing, too_much))


if __name__ == "__main__":
    unittest.main()
