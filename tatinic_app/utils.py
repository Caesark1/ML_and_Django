import numpy as np 
import pandas as pd




def main():    
    titanic_df = pd.read_csv("model/titanic.csv")
    # is_18 = titanic_df["Age"] >= 18 # if include 18 use this
    # # is_18 = titanic_df["Age"] > 18 # if not include 18 use this
    # more_than_18 = titanic_df[is_18].sort_values("Age")
    # first_10 = more_than_18.head(10)
    end_result = titanic_df[(titanic_df.Survived == 1) & (titanic_df.Age >=18)].sort_values("Age")
    first_10 = end_result.head(10)
    return first_10





