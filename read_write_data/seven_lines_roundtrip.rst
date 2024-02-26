Recap Exercise: Read and Write DataFrames
-----------------------------------------

Read the file :download:`penguin_sector.csv` into Python:

.. code:: python3

   import pandas as pd

   df = pd.read_csv('penguin_sector.csv', index_col=0, sep=',', header=0)


Solve the following tasks:

.. code:: python3

   # 1. write the data to a CSV file
   df...

   # 2. read the CSV file to a new DataFrame
   ...

   # 3. write the data to an Excel file
   ...

   # 4. read the Excel file to a new DataFrame
   ...

   # 5. write the data to a JSON file
   ...

   # 6. read the JSON file to a new DataFrame
   ...

   # 7. make sure all data frames have the same shape
   assert df.shape == ...
   