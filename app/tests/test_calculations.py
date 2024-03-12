import unittest

from app.core.calculations import ChemiCalculator


class TestChemiCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = ChemiCalculator("H2O")

    def test_calculate_molar_mass(self):
        self.assertAlmostEqual(self.calculator.formula_weight, 18.015, places=5)

    def test_get_atomic_mass(self):
        self.assertEqual(self.calculator.get_atomic_mass("H"), 1.008)
        self.assertEqual(self.calculator.get_atomic_mass("O"), 15.999)

    def test_calculate_element_percent_composition(self):
        percent_composition_H = self.calculator.calculate_element_percent_composition("H")
        percent_composition_O = self.calculator.calculate_element_percent_composition("O")

        self.assertAlmostEqual(percent_composition_H, 11.19067443796836, places=3)
        self.assertAlmostEqual(percent_composition_O, 88.80932556203163, places=3)

    def test_calculate_percent_composition(self):
        percent_compositions = self.calculator.percentage_composition

        self.assertEqual(percent_compositions[0], {'count': 2, 'element_name': 'H', 'percentage': 11.19067443796836})
        self.assertAlmostEqual(percent_compositions[1],
                               {'count': 1, 'element_name': 'O', 'percentage': 88.80932556203163})

    def test_calculate_moles(self):
        moles = self.calculator.calculate_moles(36.03)  # Mass of 2 moles of H2O
        self.assertAlmostEqual(moles, 2.0, places=1)


if __name__ == '__main__':
    unittest.main()
