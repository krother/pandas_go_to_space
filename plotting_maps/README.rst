
Plotting Maps
=============

.. figure:: earth.jpeg

`By NASA - Public Domain via Wikimedia <https://commons.wikimedia.org/w/index.php?curid=512571>`__,  also see `original source <http://visibleearth.nasa.gov/view_detail.php?id=2429http://veimages.gsfc.nasa.gov//2429/globe_east_540.jpg>`__

To Earth
--------

.. card::
   :shadow: lg

   Your sensors have picked up `a colony of pandas <http://www.panda.org.cn/>`__ on a remote class M planet.
   You suspect they are being held captive by a primitive species of two-legged aliens.
   It is also possible that the pandas are mind-controlling their captivators to treat them well.
   Your mission is to send a scouting party on the planets surface to find out.

   Your rescue team will need an accurate map of the area.

   You have the coordinates are `30.73861, 104.14276`. 
   But you are not too familiar with the local longitude/latitude system.
   Or was it latitude/longitude?

   **Just plot that map!**


The folium Library
------------------

`folium` is a Python map plotting library built on top of the JavaScript library **leaflet** (hence the name).
`folium` uses map tiles from `OpenStretMap <https://www.openstreetmap.org>`__
It produces HTML documents:

Use `pip` to install the `folium` package:

.. code::

   pip install folium


Draw a map
----------

First, define coordinates in a variable:

.. code::

   coord = (..., ...)

Then draw the map with a marker on the panda colony:

.. code::

    import folium

    colony_map = folium.Map(location=coord, zoom_start=13)
    folium.Marker(
        coord,
        popup="Panda Colony",
        icon=folium.Icon(icon="map-marker", color="blue"),
    ).add_to(colony_map)

In Jupyter, you can display the map interactively:

.. code::

    colony_map

Save the map
------------

You can save the map to a HTML file:

.. code::

   colony_map.save("colony_map.html")


.. seealso:

   `folium` can do a lot more.
   Check the documentation to find out:

   `python-visualization.github.io/folium/quickstart.html <https://python-visualization.github.io/folium/quickstart.html>`__

