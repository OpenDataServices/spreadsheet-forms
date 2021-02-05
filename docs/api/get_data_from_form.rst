get_data_from_form function
===========================

Purpose
-------

This takes a spreadsheet with user entered data and returns the data the user entered.

(Note if performance is an issue, see if using :doc:`get_data_from_form_with_guide_spec<get_data_from_form_with_guide_spec>` instead will help.)

Call
----

.. code-block:: python

    from spreadsheetforms.api import get_data_from_form

    data = get_data_from_form(
        guide_filename,
        in_filename,
        date_format=None
    )

Inputs
------

Pass:

* guide_filename - filename of the guide spreadsheet
* in_filename - filename of the input spreadsheet
* date_format - if None, any date formatted cells in the spreadsheet will be returned as Python datetime.datetime objects.
  If set, they will be turned into strings using strftime.
  For format options, see `Python docs <https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes>`_ .

Outputs
-------

Returns a JSON block of the data it managed to extract from the input.
