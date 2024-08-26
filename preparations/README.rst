
Preparations
============

.. figure:: panda_cockpit.jpeg


.. card::
    :shadow: lg

    **Boarding**

    You enter your spaceship through the airlock and take off your helmet.
    As the captain, it is your duty to be the first panda on board.
    There is an eerie silence. The ship is sleeping.
    An occasional hum from a life support console is all you can hear.
    You step through the corridors and finally reach the bridge.
    The captains seat feels comfortable, once again.
    Time to boot your spaceships computer.

    Before you can start your journey, you need to install a few programs on your ships' computer:

----

Install Python
--------------

First, you need to install a Python distribution that allows you to run the **Jupyter Notebook** format.
**Anaconda** is a one-stop installation that contains all necessary Python packages and an editing environment.

Go to `www.anaconda.com  <https://www.anaconda.com/>`__ and download Anaconda for your system (the free version) and follow the installation instructions.

.. dropdown:: Can I use VSCode instead?
   :animate: fade-in

   Yes. VSCode has a great plugin that handles the interactive Python environment.
   It is very similar to Jupyter. 
   However, I am not using it so please don't ask me for configuration details.


.. dropdown:: Can I use Google Colab?
   :animate: fade-in

   Yes. `Google Colab <https://colab.research.google.com/>`__ is free and completely cloud-based.
   When using Colab, most of the Python libraries you will need are already installed.
   However, uploading files will be a bit more tedious.
   Please look up how to do that.

.. dropdown:: Can I install packages on my own?
   :animate: fade-in

   Yes. This is a good idea if you already have a Python distribution installed on your system.
   You need to install a few core libraries.
   Use the `pip` program from a terminal to install the latest version of everything:

   .. code::

      pip install --upgrade pandas numpy seaborn matplotlib

----

Start Jupyter
-------------

- from the **Anaconda Navigator**, start the Jupyter Notebook.
- Jupyter will run as a HTTP server in the background
- From the overview page, create a new Python3 notebook with the button **New** (top-right)

Write an import section
-----------------------

Check if the core Python libraries for data analytics are installed.
Write into an empty code cell:

.. code:: python3

    import pandas as pd
    import numpy as np
    import seaborn as sns
    from matplotlib import pyplot as plt

Execute the command with the triangular *"play"* button in the toolbar or press **Shift-Enter**.
You should see an empty output and a new input cell.
If you don't see an error message, everything has worked.

----

Keyboard shortcuts
------------------

Hitting those small keys with your big paws is not easy.
It takes years of practice. To make your life easier, there are a couple of useful shortcuts: 

================ ==========================
key              description  
================ ==========================
`Shift + Enter`  execute a cell
`Escape + A`     insert a cell above
`Escape + B`     insert a cell below
`Escape + X`     delete the current cell
`Tab`            autocomplete names
`Shift + Tab`    context-sensitive help
================ ==========================

----

Edit Markdown
-------------

Edit and format a Markdown cell in Jupyter

.. code::

    ### Captains log, stardate <ENTER_TODAYS_DATE>
    
    **Captain <YOUR NAME>** has taken command of the ship *<NAME YOUR SHIP>*.

Change the type of the cell to Markdown using the icons or press `Escape + M`.

Execute the code with the **play** button on top or press `Shift + Enter`.
You should see the paragraph formatted as HTML.

----

Execute Python Code
-------------------

Write a simple new command Insert a new cell.
Check the options of the `print()` function. 
Then, run the traditional command to greet your computer:

.. code:: python

    print("hello world")

Execute the code with the **play** button on top or press `Shift + Enter`.
Your computer should respond with:

.. code::

    hello world

----

.. figure:: hello_world.jpeg

.. card::
   :shadow: lg

   It seems your ships computer is fully online.
   Time to do some more serious stuff.
