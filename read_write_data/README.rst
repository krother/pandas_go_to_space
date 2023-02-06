Read and Write Data
===================

Star Map
--------

.. figure:: planet_surface.jpeg

.. card::
   :shadow: lg

   The known universe is divided into three sectors, 
   of which the first is inhabited by giant amoeba, the second by penguins, 
   the third by cute bears called *xiong mao* in their own language, in ours simply *pandas*.
   All of them differ in their customs, operating systems and favorite programming language.
   But they are generally friendly.

   Before your spaceship can travel anywhere, you need to set a course.
   To find out where you are going, you want to load a **star map** with all three sectors:

   :download:`panda_sector.csv`

   :download:`penguin_sector.csv`

   :download:`amoeba_sector.csv`

----

Read CSV files
--------------

The ``read_csv`` function is often the first command used. It has a lot
of optional parameters, 3 of which are shown here:

.. code:: python

   import pandas as pd

   df = pd.read_csv('penguin_sector.csv', index_col=0, sep=',', header=True)

----

Read Excel files
----------------

.. code:: python

   df = pd.read_excel('penguin_sector.xlsx', index_col=0)

----

Read SQL
--------

You will need to create a DB connection first. Requires installing the
SQLAlchemy package and a DB connection package, e.g. \ ``psycopg2`` for
PostGreSQL

.. code:: python

   from sqlalchemy import create_engine

   conn = create_engine('postgres//user:psw@host:port/dbname')
   df = pd.read_sql('SELECT * FROM penguins', conn)

----

Read JSON
---------

Reading JSON only works if the structure is table-like.

.. code:: python

   df = pd.read_json('penguins.json') 

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

Plot the Star Map
-----------------

.. code:: python

   sns.scatterplot(data=df, x='x', y='z', size='size', hue='class')

----

Sources
-------

The planet names were scraped from `everybodywiki.com <https://en.everybodywiki.com/List_of_Star_Trek_planets_(A%E2%80%93B)>`__ with the following script:

.. code:: python

   import requests
   import re
   import pandas as pd
   import numpy as np

   base_url = "https://en.everybodywiki.com/List_of_Star_Trek_planets"
   char_ranges = ("AB", "CF", "GL", "MQ", "RS", "TZ")
   pattern = r'<span id="[^"]+">([^>]+)</span>|<li><b>([^>]+)</b>|<p><b>([^<]+)</b>'

   # scrape planet names
   names = []
   for char_from, char_to in char_ranges:
       url = f"{base_url}_({char_from}%E2%80%93{char_to})"
       page = requests.get(url)
       found_names = re.findall(pattern, page.text)
       print(char_from, char_to, len(found_names))
       names += [''.join(n) for n in found_names]


   # create a table with planets
   names = np.array(names)
   np.random.seed(42)  # the answer to everything
   np.random.shuffle(names)

   planets = pd.DataFrame({
       'name': names,
       'x': np.random.random(size=(n,)) * 100,
       'y': np.random.random(size=(n,)) * 100,
       'z': np.random.random(size=(n,)) * 100,
       'class': np.random.choice(np.array(list('MABC')), size=(n,)),
       'size': np.random.randint(1, 20, size=(n,)),
   })

   # write planets to files
   planets.iloc[:300].to_csv('panda_sector.csv')
   planets.iloc[300:600].to_csv('penguin_sector.csv')
   planets.iloc[600:].to_csv('amoeba_sector.csv')
