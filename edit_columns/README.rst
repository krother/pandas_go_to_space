
Edit columns
============

Planetary Descent
-----------------

.. figure:: undock.jpeg

.. card::
   :shadow: lg

   Todays mission is to examine the vegetation of a newly discovered **class M planet**.
   Because your ship is not equipped with teleportation, your researchers will have to take a shuttle to the surface.
   Your job is to bring them down safely.

   * Currently, your ship (and the shuttle) is orbiting in an altitude of **500km**.
   * Once the shuttle leaves orbit, the planets gravity accelerates the shuttle constantly by :math:`9.81 \frac{m}{s^2}`.
   * At an arbitrary moment, the shuttle can **activate its thrusters**. The thrusters thrust with an acceleration of :math:`10.0-100.0\frac{m}{s^2}`.
   * You cannot deactivate the thrusters or change their strength (this produces a lot of cleanup work and is reserved for emergencies).
   * To reach your destination on the surface, you want to reach the surface within **1500 seconds**.
  
   When should you activate the thrusters and how strong should they be?
   Let's simulate the landing to find out!

----

Create a DataFrame with a single column
---------------------------------------

Simulate the ships' altitude over time with a resolution of one second.
Start by creating the time as a column:

.. code:: python

   import pandas as pd
   import numpy as np

   seconds = np.arange(1500, dtype=np.int32)
   df = pd.DataFrame({'seconds': seconds})

The dictionary format in the parentheses allows you to define a DataFrame with multiple columns as well.

.. dropdown:: Could I use `range()` instead of `np.arange`?
   :animate: fade-in

   Yes. You would need to convert the output to a list with ``list(range(...))``.
   NumPy is faster and more flexible when you want to generate larger amounts of numbers though.
   Also you have access to C++ data types.

----

Add columns
-----------

Because the gravity does not change, we create a new column and fill it up with one value:

.. code:: python

   df['gravity'] = 9.81

For the thrust, we create a new column, settting all values to zero:

.. code:: python

   df['thrust'] = 0.0

An alternative is to create a NumPy array or list first. 
This works as long as the size of the array matches the shape of the DataFrame:

.. code:: python

   rows = df.shape[0]
   df['thrust'] = np.zeros(rows)

If you re-assign to an existing column, the old column gets replaced.

----

Modify the contents of a column
-------------------------------

Now we need to switch on the thrusters.

Fill up the bottom part of the `thrust` column with the thruster strength.
The `df.loc` allows you to access a part of a column:

.. code:: python

   activation_time = 500  # after 500 seconds
   strength = 50.0        # must be between 10.0-100.0
   df.loc[activation_time:, 'thrust'] = strength

----

Column arithmetics
------------------

We can create new columns using math equations:

.. code:: python

   df['acceleration'] = df['gravity'] - df['thrust']

To calculate the speed, we need to add all acceleration values up to a given row:

.. code:: python

   df['speed'] = df['acceleration'].cumsum()

Any calculation may include constant values.
They are applied to every row.

.. code:: python

   df['altitude [km]'] = 500 - (df['speed'].cumsum() / 1000)

----

Remove a column
---------------

The `seconds` column was useful in the beginning, so that the DataFrame was not empty.
But we do not really need it for the calculation.
To remove it, use:

.. code:: python

   df.drop('seconds', axis=1, inplace=True)

The argument `axis=1` refers to columns (`axis=0` deletes rows).
The `inplace=True` modifies the DataFrame.

----

Visualize the descent
---------------------

Let's plot the outcome of the simulation.
A simple line plot is sufficient.
We add a horizontal line to indicate the surface.

.. code:: python

   from matplotlib import pyplot as plt

   df['altitude [km]'].plot()
   plt.hlines(xmin=0, xmax=1500, y=0.0, color="red")


To debug the descent, it may help to see the speed as well.
We can show both columns in a line plot, but need to switch to a log-scale 
(both for comparability and precision).

.. code:: python

   ax = df[['altitude [km]', 'speed']].plot()
   ax.set_yscale('log')

When you see that your altitude goes through the floor of the log plot, it means that the spaceship would crash into the planet.


----

.. figure:: landing.jpeg

Challenge
---------

.. card::
   :shadow: lg

   Once you reach an altitude of **less than 100 m** and a speed of **less than 100 m/s**,
   you can activate the **anti-gravitational landing gear** that will finish the landing automatically.

   Find out values for **activation_time** and **strength**.
