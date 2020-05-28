Right field
===========


Definition
----------

Sometimes you want to allow people to put in multiple columns with the same set of headings in rows.
People can put in as few or as many columns as they want.
Each column will be converted to one JSON dictionary.
In the final data, there will be a list of JSON dictionaries.


To do this, in your cell put

.. code-block:: none

    SPREADSHEETFORM:RIGHT:listkey:itemkey

The `listkey` is the JSON key that the list of items will appear in.

All Down configurations for the same `listkey` should appear on the same row.

You should probably only have one set of right configurations per set of rows and to the right of that there should be nothing.
This is because the user can put as many data columns as they want in; if you try and put something else there it may be overwritten.

The order of the columns and the order of the items in the JSON list will be the same.

The `itemkey` is the JSON key that the data will appear in in each dictionary.

See :doc:`JSON Key for information on how to structure those<jsonkey>`.

Example
-------

A guide of:

+-------------------------------------+------------------------------------------+
| Title                               |  SPREADSHEETFORM:RIGHT:toys:title        |
+-------------------------------------+------------------------------------------+
| Does it squeak?                     |  SPREADSHEETFORM:RIGHT:toys:squeak       |
+-------------------------------------+------------------------------------------+

And a spreadsheet of:

+--------------------------+-----------------+------------------------+
| Title                    |  Plastic bone   | Tennis Ball            |
+--------------------------+-----------------+------------------------+
| Does it squeak?          |  Oh Yes         | No                     |
+--------------------------+-----------------+------------------------+

Will map to the data:


.. code-block:: json

    {
        "toys": [
            {"title": "Plastic bone", "squeak": "Oh Yes"},
            {"title": "Tennis Ball", "squeak": "No"},
        ]
    }





