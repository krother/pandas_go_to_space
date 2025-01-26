Create DataFrames and Series
============================

.. _create-dataframes-and-series-1:

Matter Transformation
---------------------

.. figure:: matter_transformer.jpeg

.. card::
   :shadow: lg
   
   Did you know that your spaceship is equipped with a powerful matter transformer?
   The matter transformer converts energy into any kind of material.
   Matter transformation is obviously a very useful invention.

   However, most of the time your crew uses the machine to make ice cream.

   Let's see how they do it.

----

**In this chapter, you learn to convert Python data structures like lists and dictionaries into pandas types like Series and DataFrames**.


Series from a Python List
-------------------------

Every element of a Python list becomes a position in the Series.
The ``index`` parameter is optional:

.. code:: python

   import pandas as pd

   flavors = pd.Series(
      ["vanilla", "chocolate", "blueberry", "bamboo"],
      index=[3, 4, 5]
   )

----

Series from a NumPy array
-------------------------

NumPy arrays convert effortlessly, because `pandas` uses them under the hood anyway.
This is especially useful to create random amounts of ice cream:

.. code:: python

   import numpy as np

   n_balls = np.random.randint(1, 10, size=4)
   s = pd.Series(
      n_balls,
      index=["vanilla", "chocolate", "blueberry", "bamboo"]
   )

----

DataFrame from a nested list
----------------------------

Nested (two-dimensional) lists convert easily to a `DataFrame`.
Adding row and column labels is fully optional.
Here is an ice cream order from a mischievous boarding party of penguins:

.. code:: python

   penguins = pd.DataFrame(
       [[1, 2, 0],
        [3, 4, None],
        [0, 0, 99],
        [0, 5, 0]],
       columns=["vanilla", "chocolate", "dynamite"],
       index=["Skipper", "Kowalski", "Rico", "Private"],
   )

----

DataFrame from a dictionary
---------------------------

When using a dictionary, the keys are used as column names, the values are lists for each column.
Note that the lists have to be of equal length.

.. code:: python

   penguins = pd.DataFrame({
       "flavor": ["vanilla", "chocolate", "blueberry", "bamboo"],
       "balls": [12, 34, 56, 78]
   })

----

DataFrame from a Numpy array
----------------------------

Numpy makes it easy to create really huge DataFrames. The index and
column names is totally optional, because consecutive numbers are used
by default.

Here is the quantum structure of tiny chocolate ice cream particle.
It is in the subatomic size and too little to be tasty,
but we thought it might be interesting to know.

.. code:: python

   data = np.random.normal(size=(100, 100))
   pd.DataFrame(data, index=range(100), columns=range(100))
