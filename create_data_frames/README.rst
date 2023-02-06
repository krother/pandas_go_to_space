Create DataFrames and Series
============================

.. _create-dataframes-and-series-1:

Matter Transformation
---------------------

.. figure:: matter_transformer.jpeg

.. card::
   :shadow: lg
   
   Did you know that your spaceship is equipped with a powerful matter transformer?
   The matter transformer converts objects into other materials.
   Matter transformation is quite useful to
   **convert Python data structures like lists and dictionaries into pandas types like Series and DataFramse**.

   However, most of the time your crew uses the machine to make ice cream.

   Below you find a few code examples.

----

Series from a Python List
-------------------------

Every element of a Python list becomes a position in the Series.
The ``index`` parameter is optional:

.. code:: python

   import pandas as pd

   s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])

----

Series from a NumPy array
-------------------------

NumPy arrays convert effortlessly, because `pandas` uses them under the hood anyway.
This is especially useful to fill columns or `DataFrames` with random numbers.

.. code:: python

   import numpy as np

   r = np.random(1, 10, size=10)
   s = pd.Series(r)

----

DataFrame from a nested list
----------------------------

Nested (two-dimensional) lists convert easily to a `DataFrame`.
The only thing you should add are the column labels unless you want to have integer numbers.

.. code:: python

   penguins = pd.DataFrame(
       [["Skipper", 12],
        ["Kowalski", 34],
        ["Rico", 56],
        ["Private", 78]],
       columns=["name", "id"])

----

DataFrame from a dictionary
---------------------------

When using a dictionary, the keys are used as column names, the values are lists for each column.
Not that the lists have to be of equal length.

.. code:: python

   penguins = pd.DataFrame({
       "name": ["Skipper", "Kowalski", "Rico", "Private"],
       "id": [12, 34, 56, 78]
   })

----

DataFrame from a Numpy array
----------------------------

Numpy makes it easy to create really huge DataFrames. The index and
column names is totally optional, because consecutive numbers are used
by default.

.. code:: python

   data = np.random.normal(size=(100, 100))
   pd.DataFrame(data, index=range(100), columns=range(100))
