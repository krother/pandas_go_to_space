
Preparations
============

Boarding
--------

.. card::
    :shadow: lg

    .. figure:: panda_airlock.png

    You enter the spaceship through an airlock. As the captain, it is your duty and privilege to be the first panda on board. There is an eerie silence. The ship is sleeping. Only an occasional hum from a life support console can be heard.
    You step through the corridors without a sound, thanks to your soft paws. You finally reach the bridge and the captains seat. Time to boot up your spaceship.

    Before you can star your journey with the **Data Starfleet**, you need to install a few programs on your ships' computer:


Install Python
--------------

First, you need to install a Python distribution that allows you to run the **Jupyter Notebook** format. **Anaconda** is a one-stop installation that contains all necessary Python packages and an editing environment.

Go to [www.anaconda.com/](https://www.anaconda.com/) and download Anaconda for your system (the free version) and follow the installation instructions.

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


Start Jupyter
-------------

- from the **Anaconda Navigator**, start the Jupyter Notebook.
- Jupyter will run as a HTTP server in the background
- From the overview page, create a new Python3 notebook with the button **New** (top-right)

Write an import section

* computer: core Python libraries for data analytics (pandas, numpy, matplotlib, seaborn)

.. code::

    import pandas as pd
    import seaborn as sns

Execute the command with the triangular *"play"* button in the toolbar or press **Shift-Enter**.

Apply keyboard shortcuts
------------------------

Hitting those small keys with your big paws is not easy.
It takes years of practice. To make your life easier, there are a couple of useful shortcuts: 

================ ===============
key              description  
================ ===============
`Shift + Enter`  execute a cell
`Escape + A`     insert a cell above
`Escape + B`     insert a cell below
`Escape + X`     delete the current cell
`Tab`            autocomplete names
`Shift + Tab     context-sensitive help
================ ===============


Write a simple new command Insert a new cell.
Check the options of the `print()` function. Then, run the traditional command to greet your computer:

    print("hello world")

Execute the command with `Shift + Enter`. Your computer should respond with:

    hello world


Edit Markdown
-------------

Edit and format a Markdown cell in Jupyter

.. code::

    ### Captains log, stardate <TODAY>
    
    **Captain <YOUR NAME>** has taken command of the ship *<NAME YOUR SHIP>*.


Create a DataFrame
------------------

Enter your data. Type the code:

.. code::

    df = pd.DataFrame([])
    df

Execute the code with the **‘play’** button on top or press **Shift-Enter**.


.. article-info::
    :avatar: images/ebp-logo.png
    :avatar-link: https://executablebooks.org/
    :avatar-outline: muted
    :author: Executable Books
    :date: Jul 24, 2021
    :read-time: 5 min read
    :class-container: sd-p-2 sd-outline-muted sd-rounded-1
