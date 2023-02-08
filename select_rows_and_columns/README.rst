Select Rows and Columns
=======================

Find your Crew
--------------

.. figure:: crew.png

.. card::
   :shadow: lg

   As a spaceship captain, you are nothing without your crew.
   There is a tradition in the Data Starfleet:
   Your five senior officers are hiding among the regular crew members, until their captain finds them.
   You assemble the entire crew on the flight dack.
   Unfortunately, it is quite hard to find someone in a crowd of 500 pandas.

   You will need to check the roster :download:`crew.csv` to identify them.

----

Show column names
-----------------

You may want to access column names as a Python list.
This is also useful to check what types the names are.

.. code:: python

   df.columns

----

Select a column
---------------

A single column is returned as a `pd.Series`:

.. code:: python

   df['id']

----

Select multiple columns
-----------------------

Takes a list of column names

.. code:: python

   df[['black_spots', 'white_spots']]

----

Select columns by position
--------------------------

The Python slicing notation can be applied to select by position.
The first slice selects all rows, the second selects columns 2-5.

.. code:: python

   df.iloc[:, 1:4]

----

Select rows by position
-----------------------

You can use the first slice only to access rows:

.. code:: python

   df.iloc[10:20]

----

Select rows by index label
--------------------------

This is very useful if your index contains something else than numbers,
e.g.

.. code:: python

   earcolor = df.set_index('ears')  # new DF with different index
   earcolor.loc['pink']

----

Filter by value
---------------

This is very powerful selection logic that is applied to all rows simultaneously.

The notation with double square brackets looks a bit weird first.
It is easier to understand if you know the inner expression results in a boolean mask that is used to filter the rows of the `DataFrame`.

.. code:: python

   df[df['ears'] == 'pink']

   df[df['black_spots'] < 3]

   df[df['black_spots'].between(3, 7)]

   df[(df['black_spots'] < 3) & (df['white_spots'] > 7)]

Note that you have to use the **binary operators** `&`, `|` to combine multiple conditions.
The **logical operators** `and`, `or` will not work.

----

Select random rows
------------------

.. code:: python

   df.sample(7)

----

.. figure:: space_panda.jpeg

Challenge
---------

.. card::
   :shadow: lg

   Select rows from the crew roster :download:`crew.csv` to find your five officers.

   Fortunately, you have a couple of hints:
   
   * the **Helmspanda** (responsible for steering the ship) has the **id 247**.
   * the **Data Science Officer** (responsible for DS of course) has **more than 18 white spots. They also have their ears dyed in indigo**.
   * the **Paw Plant** (responsible for the reactor and engines) has an **id between 100 and 199**.
   * the **Bamboo Chef** (responsible for nutrition) has **their ears dyed in chartreuse. They have fewer white spots than the paw plant**.
   * the **Pandalorian** (responsible for weapons and tactics) has an **unknown ear color**. They might be wearing a helmet.
   * all of your officers have **at least 12 white spots**.
   * three of your officers have **exactly 9 black spots**.
   * none of your officers has their **ears dyed blue**.
   
   **Identify all five of them.**
   
----

Data Generation
---------------

Below you find the code to generate the data in :download:`crew.csv`:

.. code:: python

   import pandas as pd
   import numpy as np

   np.random.seed(42)
   N = 500
   EARS = ['black', 'white', 'pink', 'blue', 'green', 'red', 'neon', 'orange', 'chartreuse', 'indigo', 'peachpuff', 'piercing', None]
   
   index = pd.Series(np.arange(N), name='id')
   
   df = pd.DataFrame(
       {
           'white_spots': np.random.randint(1, 20, size=N),
           'black_spots': np.random.randint(1, 20, size=N),
           'ears': np.random.choice(EARS, size=N)
       },
       index=index
   )
   df.to_csv('crew.csv')