Select Rows and Columns
=======================

Find your Crew
--------------

As a spaceship captain, you are nothing without your crew.
There is a tradition in the Data Starfleet:
Your five senior officers are hiding among the regular crew members, until their captain finds them.
You assemble the entire crew on the flight dack.
Unfortunately, it is quite hard to find someone in a crowd of 500 pandas.

Fortunately, you have a couple of hints on your officers:

* the **Helmspanda** (responsible for steering the ship) has the **id 247**.
* the **Data Science Officer** (responsible for DS of course) has **less than 5 white spots**.
* the **Paw Plant** (responsible for the reactor and engines) has an **id between 130 and 170**.
* the **Bamboozler** (responsible for communications) has **an ear piercing**.
* the **Pandalorian** (responsible for weapons and tactics) has an **unknown ear color**. He might be wearing a helmet.
* three of your officers have **exactly 7 black spots**.
* none of your officers has their **ears dyed blue**.
* all of your officers have **at least 4 white spots**.

Identify all five of them.

.. code:: python

   import seaborn as sns

   df = sns.load_dataset('penguins')

Show column names
~~~~~~~~~~~~~~~~~

.. code:: python

   df.columns

Select a column
~~~~~~~~~~~~~~~

.. code:: python

   df['species']

Select multiple columns
~~~~~~~~~~~~~~~~~~~~~~~

Takes a list of column names

.. code:: python

   df[['species', 'body_mass_g']]

Select columns by position
~~~~~~~~~~~~~~~~~~~~~~~~~~

Uses the Python slicing notation

.. code:: python

   df.iloc[:, 1:4]

Select the first rows
~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   df.head(3)

Select the last rows
~~~~~~~~~~~~~~~~~~~~

.. code:: python

   df.tail(3)

Select rows by position
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   df.iloc[10:20]

Select rows by index label
~~~~~~~~~~~~~~~~~~~~~~~~~~

This is very useful if your index contains something else than numbers,
e.g.

.. code:: python

   by_species = df.set_index('species') # new DF with different index

   by_species.loc['Gentoo']

Filter by value
~~~~~~~~~~~~~~~

This is very powerful selection logic

.. code:: python

   df[df['species'] == 'Adelie']

   df[df['body_mass_g'] < 3000]

   df[df['body_mass_g'].between(3000, 4000)]

Select random rows
~~~~~~~~~~~~~~~~~~

.. code:: python

   df.sample(7)
