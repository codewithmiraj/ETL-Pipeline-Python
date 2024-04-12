from etl import *

class pipeline(ETL):
  
  def __init__(self):
    self.etl = ETL()
    
  def run_pipeline(self):
    self.etl.get_data('df')
    transformed_data = self.etl.transformed_data()
    self.etl.load_transformed_data(transformed_data)
    
  
if __name__ == "__main__":
  pipeline = pipeline()
  pipeline.run_pipeline()
    

