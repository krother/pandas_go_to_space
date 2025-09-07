Read and Write Data
===================

.. figure:: planets.jpeg

.. card::
   :shadow: lg

   **Planet Data**

   The known universe is divided into three sectors, 
   of which the first is inhabited by giant amoeba, the second by penguins, 
   the third by cute bears called `xiong mao <https://chinese.yabla.com/chinese-english-pinyin-dictionary.php?define=xiong+mao>`__ in their own language, in ours simply *pandas*.
   All of them differ in their customs, operating systems and favorite programming language.
   But they are generally friendly.

   Before your spaceship can travel anywhere, you need to set a course.
   To find out where you are going, you want to load the lists of planets in all three sectors:

   :download:`panda_sector.csv`

   :download:`penguin_sector.xlsx`

   :download:`amoeba_sector.json`

----

Read CSV files
--------------

The ``read_csv`` function is often the first command used. It has a lot
of optional parameters, three of which are shown here:

.. code:: python

   import pandas as pd

   df = pd.read_csv('panda_sector.csv', index_col=0, sep=',', header=0)

``df`` is a **DataFrame**, a fundamental data structure in pandas.
For most practical matters, it works like a table.

.. dropdown:: How can I check what is in a DataFrame?
   :animate: fade-in

   After reading data into a DataFrame, you might want to see what is inside.
   It is a good idea to do that right away.
   In Jupyter, you would type into a cell:

   .. code:: python

      df

   and in a regular Python script you need an extra ``print`` statement:

   .. code:: python

      print(df)

   To see the number or rows and columns, use:

   .. code:: python

      df.shape

   Use ``print()`` in the same way outside Jupyter.
   This won't be mentioned from now on.

----

Read Excel files
----------------

Reading Excel spreadsheets works in the same way.
There is one subtle difference though: if your column labels are numbers, they are converted to integers, while `pd.read_csv()` reads them as strings. 

.. code:: python

   df = pd.read_excel('penguin_sector.xlsx', index_col=0)

.. note::

   You may need to install an extra library to read Excel files.
   Please follow the instructions in the output.

----

Read SQL
--------

You will need to create a DB connection first. Requires installing the
SQLAlchemy package and a DB connection package, e.g. ``psycopg2`` for
PostGreSQL

.. code::

   pip install psycopg2-binary
   pip install sqlalchemy

Once the library is installed, you can send SQL queries to your database and get the results as a DataFrame:

.. code:: python

   from sqlalchemy import create_engine

   conn = create_engine('postgres//user:psw@host:port/dbname')
   df = pd.read_sql('SELECT * FROM penguins', conn)

----

Read JSON
---------

Reading JSON only works if the structure is table-like.

.. code:: python

   df = pd.read_json('amoeba_sector.json') 

----

Read from Clipboard
-------------------

This is sometimes useful when improvising

.. code:: python

   df = pd.read_clipboard()

----

Concatenate multiple DataFrames
-------------------------------

When reading multiple tabular files that have the same structure,
it is sometimes straightforward to combine them into a single `DataFrame`:

.. code:: python

   df = pd.concat([df1, df2, df3, ...])

----

Writing Files
-------------

For writing a DataFrame to an output file, there is an equivalent set of functions:

.. code:: python

   df.to_csv("planets.csv")
   df.to_csv("planets.csv", index=False)  # do not write the index column

   df.to_excel("planets.xlsx")
   
   df.to_json("planets.json")

.. seealso::

   `Serialization methods in pandas DataFrames <https://pandas.pydata.org/docs/reference/frame.html#serialization-io-conversion>`__

----

.. figure:: planet_surface.jpeg

Challenge
---------

.. card::
   :shadow: lg

   How many planets are there in all three star maps combined?

----


.. include:: seven_lines_roundtrip.rst

----

.. dropdown:: Where do the planet names come from?
   :animate: fade-in

   The planet names were scraped from `everybodywiki.com <https://en.everybodywiki.com/List_of_Star_Trek_planets_(A%E2%80%93B)>`__ with the following script:

   .. literalinclude:: planet_scraper.py
