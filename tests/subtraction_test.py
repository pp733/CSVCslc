"""Testing Subtraction"""
import pandas as pd
from calc.calculations.subtraction import Subtraction

def test_calculation_subtraction():
    """testing that our calculator has a static method for addition"""
    df = pd.read_csv("CSVFiles/Subtraction.csv")
    print(df.head(5))
    for x, y in df.iterrows():
        sub = (y.Value_1, y.Value_2)
        subtraction = Subtraction.create(sub)
        assert subtraction.get_result() == df['Result'][x]