"""Testing Addition"""
<<<<<<< HEAD
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
=======
from calc.calculations.addition import Addition

def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (1.0,2.0)
    addition = Addition(mynumbers)
    #Act
    #Assert
    assert addition.get_result() == 3.0
>>>>>>> origin/part5
