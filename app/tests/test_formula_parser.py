import unittest

from app.core.calculations import ChemiCalculator


class TestParseFormula(unittest.TestCase):

    def test_simple_formula(self):
        formula = "H2O"
        formula = self.calculator = ChemiCalculator(formula)
        expected = {'H': 2, 'O': 1}
        self.assertEqual(expected, formula.element)

    def test_complicated_formula(self):
        formula = "H2SO4"
        formula = self.calculator = ChemiCalculator(formula)
        expected = {'H': 2, 'S': 1, 'O': 4}
        self.assertEqual(expected, formula.element)

    def test_formula_with_parentheses(self):
        formula = "(H2O)3"
        formula = self.calculator = ChemiCalculator(formula)
        expected = {'H': 6, 'O': 3}
        self.assertEqual(expected, formula.element)

    def test_complicated_formula_with_parentheses(self):
        formula = "((H2O)3)2"
        formula = self.calculator = ChemiCalculator(formula)
        expected = {'H': 12, 'O': 6}
        self.assertEqual(expected, formula.element)

    def test_formula_with_mixed_atoms(self):
        formula = "C6H12O6"
        formula = self.calculator = ChemiCalculator(formula)
        expected = {'C': 6, 'H': 12, 'O': 6}
        self.assertEqual(expected, formula.element)

    def test_formula_with_mixed_atoms_and_parentheses(self):
        formula = "C6(H2O)3"
        formula = self.calculator = ChemiCalculator(formula)
        expected = {'C': 6, 'H': 6, 'O': 3}
        self.assertEqual(expected, formula.element)


if __name__ == '__main__':
    unittest.main()
