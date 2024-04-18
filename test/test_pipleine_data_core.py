import pytest
import pandas as pd 
import numpy as np 

@pytest.fixture
def df():
  df = pd.read_csv(r"C:\Users\Miraj\Downloads\sales_data_sample.csv",encoding="latin-1")
  return  df

#check if column exist 
def test_col_exists(df):
  name = "SALES"
  assert name in df.columns
  
#check for NaN values
def test_null_check(df):
  assert np.where(df["SALES"].isnull())
  
#check values in range
def test_range_val_str(df):
  assert df["SALES"].between(0,10000).any()
  
  