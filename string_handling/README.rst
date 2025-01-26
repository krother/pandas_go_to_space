
String Handling
===============

.. figure:: delegate.jpeg

Diplomacy
---------

.. card::
   :shadow: lg

   You finally make direct contact with the space penguins.
   Their delegates meet yours. All of you have brushed your fur diligently and bring the tastiest bamboo leaves as a gift of friendship.
   When you board the penguins' ship, the meeting is a bit frosty.
   First, they iced the floor and your diplomats slip and roll around a couple of times.
   Next, upon seeing your gift the penguins hand you a slimy, smelly object.

   **You can't think of anything more rude! Is this a provocation? Is peace in the galaxy at stake?**

   Then the head of the penguin delegation starts to speak:

   .. code::

      pokHaELlRlnoXprrr purSAtfrQADnLgXeCprrr pukCprpEaAmtcuprZeSSEprrr
      pokwzIITihFprrr plofIUuRkprrr plosztnOfPhprrr prtWrEhprrr 
      pokayRYEdprrr prttqHOEJprrr plopPelnLGAUzIdNGShprrr ploSOtNOlPIprrr
      pukWreYprrr pukcCoUMpEFprrr purifnSprrr pukPrEXAgcaEJprrr prtSrTUOUPKprrr
      pokpilQeDAZScEmprrr purThAZKIeeprrr purTIhmiksUprrr ploTzAcsFTwYkprrr
      plofcIGsWhSprrr pokaesGprrr prtauprrr pokWAeOLVCfOUMoELprrr
      pukgGIOFITDprrr prtsKtROBPcprrr puksgHNaiLLLtprrr pukWsEqprrr
      poksYHCokwxprrr pokYLOzUFprrr pokTLOuprrr pukOBuhRdprrr
      puksvWuiZMYmpIQNfgyprrr purPxOuoYLEprrr puksYtlOHPWprrr
   
   Your translation computer quickly starts analyzing the penguin language.
   Let's find out what the penguins have to say.

----

Tokenization
------------

Let's feed the entire message into pandas:

.. code:: python

   text = """pokhrEYLMLAohprrr ploWdoBRKledYprrr"""
   df = pd.DataFrame({'text': [text]})

You should have a ``DataFrame`` with a single row that contains the entire text.
Let's split the text into words.
The ``.str`` attribute of a ``pd.Series`` gives you an access point to Python string functions:

.. code:: python

   words = df["text"].str.split()

Having a list inside a ``pd.Series`` is not too easy to read.
It is better to unfold every word into a single row:

.. code:: python

   s = words.explode()

And convert the resulting Series to a nicely indexed ``DataFrame``:

.. code:: python

   df = pd.DataFrame({"words": s}).reset_index(drop=True)

----

Slicing Strings
---------------

Your translation computer found out that every word starts with a **glacial phoneme**.
These are any of the syllables *"plo", "pok", "pur", "prt"* or *"puk"* describing the current temperature. Because your life support keeps temperature constant, you can ignore these.

Let's remove the first three characters.
You can use ``.str`` to slice the strings in the entire column:

.. code:: python

   df["words"].str[3:]

Every word ends with the syllable *"prrr"*, an **arctic morpheme** which means something like *"it's cold here"*. This is obvious and can be ignored as well.

Every second character is a *prosodial psychronic phoneme* which is quite important in a conversation with other penguins, but in interstellar diplomacy we can leave it out as well.

Insert numbers for *start, stop* and *step* into the slicing expression
to get rid of all the morphemes and phonemes.

.. code:: python
   
   df["words"].str[start:end:step]
   
Assign the result to a new column.

----

Case Conversion
---------------

Words in the penguin language consist of a mix of uppercase and lowercase characters.
The case indicates how much the speaker is freezing (lowercase=a little, uppercase=a lot).
The methods ``.str.upper()`` and ``.str.lower()`` allow to change case for an entire string column:

.. code:: python
   
   df["words"].str.lower()

Because of our dense fur, the cold doesn't affect us much.
Convert to everything to lower case.

----

Join Words
----------

Once the computer is done translating all the words, you might want to put them into a single piece of text again.
Because Python can iterate over columns of a DataFrame, you can use the normal `.join()` method of a string:

.. code:: python
   
    " ".join(df["words"])

----

Word Length
-----------

For a deeper scientific analysis of the penguin language, the word length might be useful:

.. code:: python

   df["words"].str.len()

----

String Search
-------------

Strings in pandas columns can be searched with **Regular Expressions**.
You can use the ``.findall()`` function and pattern syntax from the ``re`` module:

.. code:: python

   import re

   df['words'].str.findall(r'h.e.l.l.o', re.IGNORECASE)

----

Translate Back
--------------

It is time to respond the penguin delegation.
Your translation computer has developed an algorithm that translates panda language back to penguin language:

.. code:: python

   import string
   from random import choice
   
   def random_char_gen():
       while True:
           yield choice(string.ascii_lowercase + string.ascii_uppercase)
               
   def translate_pan_to_peng(word):
       chars = ""
       for a, b in zip(word, random_char_gen()):
           chars += choice([a.lower, a.upper])()
           chars += b
       prefix = choice(["plo", "pok", "pur", "prt", "puk"])
       postfix = 'prrr'
       return prefix + chars + postfix
   
   message = "..."
   words = [translate_pan_to_peng(w) for w in message.split()]
   translated = ' '.join(words)

**Write an aproppriate response and translate it to pingu-speak.**
