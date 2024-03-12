from typing import Any

from chemformula import ChemFormula

from app.constants.atomic_masses import get_element_mass_mapping

atomic_masses = get_element_mass_mapping()


class ChemiCalculator(ChemFormula):
    def __init__(self, formula):
        super().__init__(formula)
        self.percentage_composition = self.calculate_percent_composition()


    @staticmethod
    def get_atomic_mass(element: str) -> float:
        return atomic_masses.get(element, 0)

    def calculate_element_percent_composition(self, element: str) -> float:
        """
        Calculate the percent composition of a specific element in a compound.

        Parameters:
        - formula (str): Chemical formula of the compound.
        - element (str): Chemical symbol of the element.

        Returns:
        - float: Percent composition of the specified element.
        """
        element_mass = self.element[element] * atomic_masses[element]
        percent_composition = (element_mass / self.formula_weight) * 100
        return percent_composition

    def calculate_percent_composition(self) -> list[dict[str, float | Any]]:
        """
        Calculate the percent composition of a specific element in a compound.

        Parameters:
        - formula (str): Chemical formula of the compound.
        - element (str): Chemical symbol of the element.

        Returns:
        - float: Percent composition of the specified element.
        """
        compositions = []

        for element, count_ in self.element.items():
            percent_composition = self.calculate_element_percent_composition(element)
            compositions.append({"element_name": element, "count": count_, "percentage": percent_composition})
        return compositions

    def calculate_moles(self, mass: float) -> float:
        """
        Calculate the number of moles of a compound given its mass and formula.

        Parameters:
        - mass (float): Mass of the compound in grams.
        - formula (str): Chemical formula of the compound.

        Returns:
        - float: Number of moles of the compound.
        """
        return mass / self.formula_weight


if __name__ == "__main__":
    h20 = ChemiCalculator("H2O")
    print(h20.formula_weight)
    print(h20.calculate_element_percent_composition("O"))
    print(h20.calculate_moles(13.3))
