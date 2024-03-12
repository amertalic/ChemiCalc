# ChemiCalc Fast API App

ChemiCalc is a simple Python FastAPI application designed to assist users in performing basic calculations related to chemical formulas. 
This app allows users to input chemical formulas and receive various calculated results.

## Prerequisites

- Python 3.11
- FastAPI

## Installation

1. Clone the repository

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the FastAPI application:

    ```bash
    uvicorn main:app --reload
    ```

2. Open your browser and navigate to `http://localhost:8000` to access the ChemiCalc homepage.

3. On the homepage, enter a chemical formula in the provided form (e.g., H2O) and click the "Calculate" button.

4. You will be redirected to the results page, where the following calculations are displayed:
    - Chemical Formula with Subscripted Integers (formatted correctly)
    - Calculated Molar Mass
    - Percentage Composition
    - Moles on 1000 Grams

5. To perform calculations for another chemical formula, simply submit a new formula on the results page by entering it in the form and clicking the "Submit" button.

## Supported Results

ChemiCalc currently supports the following results:

1. **Chemical Formula with Subscripted Integers:**
    - The chemical formula is displayed with proper subscript formatting.

2. **Calculate Molar Mass:**
    - The molar mass of the entered chemical formula is calculated and displayed.

3. **Percentage Composition:**
    - The percentage composition of each element in the chemical formula is displayed.

4. **Moles on 1000 Grams:**
    - The number of moles for each element per 1000 grams of the compound is displayed.
