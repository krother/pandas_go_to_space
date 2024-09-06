
Powerful Pivots
===============

Goal
----

In this set of exercises, you will analyze the `Berkeley's 1973 Graduate Admissions Dataset <https://discovery.cs.illinois.edu/dataset/berkeley/>`__.
In particular, we want to find out **whether the admissions were gender biased.**

To solve the task, you will need a healthy mix of **data wrangling** and **aggregation**.
Eventually you will come across **Simpsons Paradoxon**.


Exercise 1: Load the data
-------------------------

You can find the data on `https://discovery.cs.illinois.edu/dataset/berkeley/ <https://discovery.cs.illinois.edu/dataset/berkeley/>`__.
To conveniently load the data, place the URL of the CSV file into the `pd.read_csv()` command instead of the file name. `pandas` does the rest.

**Inspect a few rows of the resulting DataFrame.**

Exercise 2: Quality checks
--------------------------

You may want to perform a couple of quality checks:

- How many rows and columns does the dataset have?
- Use `df.info()` to check the data types.
- Use `df[colname].value_counts()` to check what categories the columns have.
- Use `df.isna().sum()` to check for missing values.

Exercise 3: Simple aggregation
------------------------------

Next, summarize how many students passed the admissions in total.
For that you need to aggregate by the `Admission` column and count the rows:

.. code:: python3

    s = df.groupby(col)[col2].count()

Note that `col2` can be any of the other columns.
The result is a `pd.Series` (a single column of data) that can be plotted easily:

.. code:: python3

   s.plot.bar()
   s.plot.pie()

If you prefer **relative frequencies**, you can **normalize** the aggregated Series
using column arithmetics:

.. code:: python3

   perc = s / s.sum()

.. hint::

   The percentage is the **probability of acceptance** if we know nothing about the student.
   This knowledge-less probability is also called a **prior**.

Exercise 4: Count departments
-----------------------------

Repeat the aggregation to count how many applicants each of the departments had.

Exercise 5: Remove the long tail
--------------------------------

We do not really know what is going on in the `Other` departments.
To remove these entries completely, use

.. code:: python3

   df2 = df[df["Major"] != "Other"]

After removing the entries, you could still do the same plotting as before.

.. warning::

    Consider the following pie chart:

    .. code:: python3

        df2.groupby("Major")["Year"].sum().plot.pie()

    Why is this plot wrong, whereas the corresponding bar chart is ok?


Exercise 6: Boolean categories
------------------------------

Sometimes it is helpful to convert a column with two distinct values to a number.
For instance, you could create an integer admission column:

.. code:: python3

    df["Admission"].replace({"Rejected": "0", "Accepted": "1"}).astype(int)

Or the same as a boolean (that doubles as an integer as well).

.. code:: python3

    df["Admission"] == "Accepted"

Assign the new column to the DataFrame with `df[newcol] = `.

Exercise 7: Gender Bias
-----------------------

The new integer column helps to quantify the gender bias.
Use the `.mean()` function on the new column:

.. code:: python3

   df.groupby(col)[newcol].mean()

Use `.plot.bar()` to display the results.

**How would you interpret the result?**

Exercise 8: Aggregate by two categories
---------------------------------------

An alternative for the above aggregation is to use `df.groupby()` with two categorical variables:

.. code:: python3

   df.groupby(["Gender", "Admission"])["Year"].count()

The result come out in the **long format** using a MultiIndex that we will deal with in another exercise.
To convert it back into a DataFrame, add `.unstack()` to the line.

Exercise 9: Pivot
-----------------

A different name for the double-category aggregation is a **pivot table**.

Create a pivot table, calculating the admission rate for each gender/major combination.

**How would you interpret the result?**

.. hint::

    This is where you may see a phenomenon called *"Simpsons Paradox"*.

Exercise 10: Plots
------------------

Consider the pivot table of counts:

.. code:: python3

   pt = df.groupby(["Major", "Gender"])["Year"].count().unstack()

You could plot it quite nicely with:

.. code:: python3

   pt.plot.bar()

or

.. code:: python3

    import seaborn as sns

    sns.heatmap(pt, annot=False)


Exercise 11: Conditional Probabilities
--------------------------------------

As a last step, normalize the pivot table by a sum.
Compare the following commands:

.. code:: python3

   pt / pt.sum()

   pt.T / pt.T.sum()

   pt / pt.sum().sum()

What are the differences between the three commands?

.. hint::

    for a deeper reflection, look up the concept of **Conditional probability.**

Reflection Questions
--------------------

- what types of aggregation are possible with pandas?
- what is the difference between absolute and relative frequency?
- how could a statistics be misleading with Simpsons Paradox?
- how could you prevent falling victim to Simpsons Paradox?


.. seealso::

   `more about Simpsons Paradox <https://discovery.cs.illinois.edu/learn/Basics-of-Data-Science-with-Python/Simpsons-Paradox/>`__
