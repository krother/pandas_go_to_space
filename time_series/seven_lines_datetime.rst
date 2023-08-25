
Recap Exercise: Datetime Indexes
--------------------------------

To prepare for the challenge, create 30 random numbers:

.. code:: python3

   import numpy as np

   data = np.random.randint(1, 7, size=30)

Solve the following tasks:

.. code:: python3
   
   # 1. create timestamps for an entire April, one per day
   ...

   # 2. display the year for each timestamp
   ...

   # 3. display the weekday for each timestamp
   ...

   # 4. create a Series with the random data and the timestamps as index
   ...

   # 5. select the timestamps until the 11th
   ...

   # 6. calculate the sum of all numbers for each week
   ...

   # 7. calculate a rolling average with a 7-day window
   ...
