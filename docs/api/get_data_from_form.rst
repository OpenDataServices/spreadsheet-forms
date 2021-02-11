get_data_from_form function
===========================

Purpose
-------

Extracts JSON data from a spreadsheet form, based on a structure specified in a guide form.

If performance is an issue, see  :doc:`get_data_from_form_with_guide_spec<get_data_from_form_with_guide_spec>`.

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

Returns a JSON representation of the data extracted from the form.
