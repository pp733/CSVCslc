"""Testing Addition"""
import pandas as pd
from calc.calculations.division import Division

def test_calculation_division():
    """testing division method with csv inputs"""
    df = pd.read_csv("CSVFiles/Division.csv")
    print(df.head(3))
    for x, y in df.iterrows():
        div = (y.Value_1, y.Value_2)
        division = Division.create(div)
        try:
            assert division.get_result() == df['Result'][x]
        except ZeroDivisionError:
            print("Cannot divide by zero")