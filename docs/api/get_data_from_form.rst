get_data_from_form function
===========================

.. code-block:: python

    data = get_data_from_form(
        guide_filename,
        in_filename,
        get_data_from_form=None
    )

Pass:

* guide_filename - filename of the guide spreadsheet
* in_filename - filename of the input spreadsheet
* get_data_from_form - if None, any date formatted cells in the spreadsheet will be returned as Python datetime.datetime objects.
  If set, they will be turned into strings using strftime.
  For format options, see `Python docs <https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes>`_ .

Returns:

* data - a JSON block of the data it managed to extract from the input