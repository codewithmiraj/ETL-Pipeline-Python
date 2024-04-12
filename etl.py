import pandas as pd 

class ETL():
  
  def __init__(self):
    pass
  
  '''retrieve our data'''
  
  def get_data(self,df):
    self.df = df
    self.df = pd.read_csv("C:\\Users\\Miraj\Downloads\\sales_data_sample.csv",encoding="latin-1")
    self.df.head()
    print(self.df)
  
  '''clean and preprocess data'''
  
  def transformed_data(self):
    self.df.drop_duplicates(inplace=True) # removing duplicates 
    self.df.dropna(inplace=True) # removing NaN values
    # Print cleaned data
    print("Transformed Data:")
    print(self.df)
    return self.df
      
  '''load data back for storage'''
   
  def load_transformed_data(self, transformed_data, filename="transformed_data.csv"):
    transformed_data.to_csv(filename, index=False)
    print(f"Transformed data saved for storage: {filename}")

retrieved_data = ETL()
retrieved_data.get_data('df')
transformed_data = retrieved_data.transformed_data()
retrieved_data.load_transformed_data(transformed_data, "transformed_data.csv")




