Examples
========


A Guide Form spreadsheet
------------------------

.. |_| unicode:: 0xA0
   :trim:


A guide form spreadsheet is the template to show us where to expect data. Any operation will need one of these to guide it.

These have special values in certain cells - this tells the library where and how to manipulate data.

For example:

+----------------------------------------+------------------------------------------+
| **Pet**                                |  SPREADSHEETFORM:SINGLE:pet              |
+----------------------------------------+------------------------------------------+
| |_|                                    |                                          |
+----------------------------------------+------------------------------------------+
| **Toys:**                              |                                          |
+----------------------------------------+------------------------------------------+
| **Title**                              |  **Does it squeak?**                     |
+----------------------------------------+------------------------------------------+
| SPREADSHEETFORM:DOWN:likes/toys:title  |  SPREADSHEETFORM:DOWN:likes/toys:squeak  |
+----------------------------------------+------------------------------------------+

Extracting data from a spreadsheet
----------------------------------

Given the guide spreadsheet above and a spreadsheet with data in it, like:

+-------------------------------------+------------------------------------------+
| **Pet**                             |  Dog                                     |
+-------------------------------------+------------------------------------------+
| |_|                                 |                                          |
+-------------------------------------+------------------------------------------+
| **Toys:**                           |                                          |
+-------------------------------------+------------------------------------------+
| **Title**                           |  **Does it squeak?**                     |
+-------------------------------------+------------------------------------------+
| Plastic bone                        |  Oh Yes                                  |
+-------------------------------------+------------------------------------------+
| Tennis Ball                         |  No                                      |
+-------------------------------------+------------------------------------------+

The function :doc:`get_data_from_form<api/get_data_from_form>` will produce the following data:

.. code-block:: json

    {
        "pet": "Dog",
        "likes": {
            "toys": [
                {"title": "Plastic bone", "squeak": "Oh Yes"},
                {"title": "Tennis Ball", "squeak": "No"}
            ]
        }
    }

Note the SINGLE keyword is turned into a field, but the DOWN row is turned into a list.
People can add as many or as few items to the DOWN table as they want.

Putting data into a spreadsheet
-------------------------------

The process can be run in reverse using the :doc:`put_data_in_form<api/put_data_in_form>` function.

Given the JSON data above, the function will produce the spreadsheet above.