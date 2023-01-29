
The Python DS Ecosystem
=======================

.. card::
    :shadow: lg

    .. figure:: panda_airlock.png

    You enter the spaceship through an airlock. As the captain, it is your duty and privilege to be the first panda on board. There is an eerie silence. The ship is sleeping. Only an occasional hum from a life support console can be heard.

    You step through the corridors without a sound, thanks to your soft paws. You finally reach the bridge and the captains seat. Time to boot up your spaceship.

    Before you can star your journey with the **Data Starfleet**, you need to install a few programs on your ships' computer:


Install Python
--------------

check the main computer.
* go on your spaceship, the Jupyter: install a Jupyter based Python environment (preferably Anaconda).

.. dropdown:: Can I use Google Colab?
   :animate: fade-in

   Yes, you can. Google Colab LINK is free and completely cloud-based.
   When using Colab, most of the Python libraries you will need are already installed.
   However, uploading files will be a bit more tedious.
   Please look up how to do that.

Install libraries
-----------------

You will need a couple of Python libraries for analyzing space data.
* computer: core Python libraries for data analytics (pandas, numpy, matplotlib, seaborn)
* clean up the captains quarters

Write an import section

.. code::

    import pandas as pd

Execute the command with the triangular *"play"* button in the toolbar.

Apply keyboard shortcuts
------------------------

Hitting those small keys with your big paws is not easy.
It takes years of practice. To make your life easier, there are a couple of useful shortcuts: 

insert cell with `Esc + A` or `Esc + B`
help `SHIFT-TAB`
use the auto-completion `TAB`

Check the options of the `print()` function. Then, run the traditional command to greet your computer:

    print("hello world")

Execute the command with `Shift + Enter`. Your computer should respond with:

    hello world

Edit Markdown
-------------

* edit and format a Markdown cell in Jupyter

.. code::

    ### Captains log, stardate <TODAY>
    
    **Captain <YOUR NAME>** has taken command of the ship *<NAME YOUR SHIP>*.

Create a DataFrame
------------------

from scratch: captains data


.. article-info::
    :avatar: images/ebp-logo.png
    :avatar-link: https://executablebooks.org/
    :avatar-outline: muted
    :author: Executable Books
    :date: Jul 24, 2021
    :read-time: 5 min read
    :class-container: sd-p-2 sd-outline-muted sd-rounded-1
