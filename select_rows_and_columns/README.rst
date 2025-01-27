Select Rows and Columns
=======================

.. figure:: crew.png

.. card::
   :shadow: lg

   **Find your Crew**

   As a spaceship captain, you are nothing without your crew.
   You have five capable officers that help you run things.
   Unfortunately, you have no idea where they are.
   You assemble the entire crew on the flight deck.
   How did your officers look like again?
   
   You will need to load the crew roster :download:`crew.csv` to identify them.

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

Multiple columns require double square brackets.
The inner one is a list of column names:

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
   You have a couple of hints:
   
   * all of your officers have **at least 12 white spots**.
   * three of your officers have **exactly 9 black spots**.
   * none of your officers has **white ears** or **black ears**.
   * the **Helmspanda** (responsible for steering the ship) has the **id 247**.
   * the **Data Science Officer** (responsible for DS of course) has **more than 18 white spots. They also have their ears dyed in indigo**.
   * the **Paw Plant** (responsible for the reactor and engines) has more white spots than the Pandalorian.
   * the **Pandalorian** (responsible for weapons and tactics) has an **unknown ear color**. They wear a helmet all the time.
   * the **Bamboo Chef** (responsible for nutrition) has **their ears dyed in chartreuse. They have fewer white spots than the paw plant**.
   
   **Identify all five of them.**

.. dropdown:: How many white spots do your officers have in total?
   :animate: fade-in

   There should be exactly 79.

----

.. dropdown:: How was the crew data generated?
   :animate: fade-in

   Below you find the code to generate the data in :download:`crew.csv`:

   .. literalinclude:: crew_generator.py
