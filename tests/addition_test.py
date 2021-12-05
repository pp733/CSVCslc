"""Testing Addition"""
import pandas as pd
from calc.calculations.addition import Addition

def test_calculation_addition():
    """testing addition method with csv inputs"""
    df = pd.read_csv("CSVFiles/Addition.csv")
    print(df.head(5))
    for x, y in df.iterrows():
        sum = (y.Value_1, y.Value_2)
        addition = Addition.create(sum)
        assert addition.get_result() == df['Result'][x]