import pytest
import pandas as pd 
import numpy as np 

df = pd.read_csv(r"C:\Users\Miraj\Downloads\sales_data_sample.csv",encoding="latin-1")

#check if column exist 
def test_col_exists():
  name = "SALES"
  assert name in df.columns
  
#check for NaN values
def test_null_check():
  assert np.where(df["SALES"].isnull())
