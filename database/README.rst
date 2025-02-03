
The Duck Archives
=================

.. card::
   :shadow: lg

   **Long-term-memory**

   Before you launch, you need to create a backup of all important data.
   You head for a duck with a fantastic memory and tell them everything.

   The duck speaks a strange language though - SQL.


Installing DuckDB
-----------------

DuckDB is a Python library. Install it with:

.. code::

   !pip install duckdb

Read Data
---------

Like pandas, duckdb can read data directly from CSV files and other formats.

.. code:: python3

    import duckdb
    
    panda_sector = duckdb.read_csv("panda_sector.csv", index_col=0)
    df = panda_sector.to_df()

SQL Queries
-----------

With SQL, you can answer questions to the data:

.. code:: python3

    duckdb.sql("SELECT * FROM 'panda_sector.csv' WHERE class='M'")
    duckdb.sql("SELECT name,size FROM 'panda_sector.csv' WHERE class='M' AND size> 10 ORDER BY name LIMIT 10")

Note that you can refer to tables by the file path or by a Python variable name:

.. code:: python3

    duckdb.sql("SELECT * FROM panda_sector LIMIT 5").df()
  
Store the Database in a file
----------------------------

So far, eveything was stored in memory only.
Lets' make it persistent:

.. code:: python3

    con = duckdb.connect("starbase.db")
    con.read_csv("panda_sector.csv")
    con.sql("CREATE TABLE dummy AS SELECT * FROM 'panda_sector.csv' LIMIT 5")
    con.close()
  
Now you should see a file `starbase.db` .

.. code:: python3

   con = duckdb.connect("file.db")
   con.sql("SELECT * FROM dummy")
  

.. seealso::

   `https://duckdb.org/docs/api/python/dbapi <https://duckdb.org/docs/api/python/dbapi>`__
