Examples
========


A Guide Form spreadsheet
------------------------

.. |_| unicode:: 0xA0
   :trim:


A guide form spreadsheet is a template that specifies the structure of a spreadsheet form. All functions require a guide form.

Guide forms use special values in certain cells to specify the structure of a spreadsheet form.

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

Given the guide form above and the following populated spreadsheet form:

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
The people filling in the spreadsheet can add as many or as few items to the DOWN table as they want.

Populating a spreadsheet form
-----------------------------

The process can be run in reverse using the :doc:`put_data_in_form<api/put_data_in_form>` function.

Given the JSON data above, the function will produce the populated spreadsheet form above.

