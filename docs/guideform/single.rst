Single field
============

Definition
----------

Sometimes you want a single cell in the spreadsheet to be represented by a single JSON value in the data.

To do this, in your cell put

.. code-block:: none

    SPREADSHEETFORM:SINGLE:jsonkey


Note the `jsonkey` must be a single key and can not contain paths yet; eg "pet" is acceptable, "pet/title" is not.

Example
-------

A guide of:

+---------+--------------------------------------+
| Pet     |  SPREADSHEETFORM:SINGLE:pet          |
+---------+--------------------------------------+

And a spreadsheet of:


+---------+--------------------------------------+
| Pet     |  Cat                                 |
+---------+--------------------------------------+

Will map to the data:


.. code-block:: json

    {
        "pet": "Cat"
    }

