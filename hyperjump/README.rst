
Hyperjump
=========

.. card::
   :shadow: lg

   .. figure:: hyperjump.png

   It's time to activate the hyperdrive and make a long-distance leap through space.
   Hyperjumps are a complicated matter. Your crew needs to gracefully increase the speed of the spaceship until you reach **jump speed (JS)**. 
   Jump too early or too late and your ship will be torn to pieces.
   Jump to the wrong coordinates, and you end up inside a planet or a black hole.
   Of course, the computer does most of the math, but the main calculation needs to be double-checked.
   

* At jump-speed, the **space fold** and **time fold** are exactly equal.

  space fold : exp(speed * a1 + G)
  time fold : exp(speed * a2 + a3)

* G is the **gravitational jitter**. It looks like random numbers, but depends on the universal constant 42.

Gravity calibration

  gravitational_jitter(speed): random normal

  find out where space - time fold == 0

* plot: line plot with log scale
* random signal
* apply a log-transform on a column
* revert a log-transform by exp()
* decide whether a column should be log-transformed
