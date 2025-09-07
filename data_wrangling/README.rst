Data Wrangling
==============

Cargo Bay
---------

.. figure:: containers.jpeg

.. card::
   :shadow: lg

   One day you decide to inspect the cargo bay of your spaceship.

   What a mess!

   Many of the containers are badly labeled.
   The radioactive waste is next to the ice cream.
   Some containers are not labeled at all.

   Time for a proper cleanup of the cargo docs in :download:`cargo.csv`. 

----

Sort rows
---------

Sort a DataFrame by:

.. code:: python

   df.sort_values(by="category", inplace=True)

to sort by more than one column, try:

.. code:: python

   df.sort_values(by=["category", "type"], ascending=[True, False], inplace=True)


Change the data type
--------------------

Convert values to strings:

.. code:: python

   df["crate_str"] = df["crate_no"].astype(str)

You can easily combine multiple columns using standard operators:

.. code:: python

   df["crate_id"] = df["crate_no"].astype(str) + df["crate_shelf"]

Create new rows
---------------

If you have Python sequence types (lists, tuples, sets), you can assign them to new columns directly.
The only prerequisite is that the length matches that of your DataFrame:

.. code:: python

   deck = [d for _,d in zip(range(df.shape[0]), cycle("123"))]  # repeat 1,2,3,1,..
   df["deck"] = deck 

Set the index column
--------------------

The index is a special column of a DataFrame, because it is treated
differently by many operations in pandas.

.. code:: python

   # put the new crate_id column in the index
   crates = df.set_index('crate_id')

   # now you can select by crate_id easily:
   crates.loc['13A']

Note that the ``inplace=True`` parameter modifies the DataFrame instead
of returning a new one:

.. code:: python

   df.set_index('crate_id', inplace=True)

The `inplace=True` notation is more memory-efficient, but it is more tricky in Jupyter
notebooks (e.g. when you run that line twice you get different results.

To move the index to a regular column, use:

.. code:: python

   df_reset = df.reset_index()  # inserts a numerical index starting from 0

Missing values
--------------

Missing values are a common phenomenon. A quick way to diagnose missing
values is:

.. code:: python

   df.isna().sum().plot.bar()

Often, you might simply want to kick out all rows in which a None or NaN
occurs:

.. code:: python

   df_dropped = df.dropna(inplace=False)  # same logic as with set_index()

Alternatively, you might want to fill in a best guess value:

.. code:: python

   df_fixed = df.fillna(42)
   # or
   df_fixed = df.fillna(df.median())

There are many, many strategies to fix missing values (imputation
methods).

Swap rows and columns
---------------------

Some operations (especially plotting) are easier to implement if you
turn a DataFrame by 90°:

.. code:: python

   df.transpose()

Iterate
-------

Usually, it is possible to write one-liners or concise expressions that
get the job done. If this is not possible (or you are still learning
this stuff and can’t figure out a better way yet), you may want to fall
back to a ``for`` loop over all the rows.

.. code:: python

   for index, row in df.iterrows():
       print(index, row['type'])


.. figure:: bamboo.jpg

Challenge
---------

.. card::
   :shadow: lg

   Take care of the following clean-ups in the cargo docs :download:`cargo.csv`:

   - for the radioactive waste, replace the words in the `units` column by numbers
   - convert the `units` column to the type `int`
   - fill the missing values in the `category` column for the bamboo ice cream
   - fill the missing values in the `units` column
   - sort the crates by type and by identifier in ascending order
  