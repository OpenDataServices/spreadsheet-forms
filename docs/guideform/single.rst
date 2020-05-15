Single field
============

Definition
----------

Sometimes you want a single cell in the spreadsheet to be represented by a single JSON value in the data.

To do this, in your cell put

.. code-block:: none

    SPREADSHEETFORM:SINGLE:jsonkey


See :doc:`JSON Key for information on how to structure those<jsonkey>`.

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

