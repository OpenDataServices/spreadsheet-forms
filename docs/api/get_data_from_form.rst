get_data_from_form function
===========================

Purpose
-------

Extracts JSON data from a spreadsheet form, based on a structure specified in a guide form.

If performance is an issue, see  :doc:`get_data_from_form_with_guide_spec<get_data_from_form_with_guide_spec>`.

Call
----

.. code-block:: python

    from spreadsheetforms.api import get_data_from_form, GetDataFromFormMissingWorksheetAction

    data = get_data_from_form(
        guide_filename,
        in_filename,
        date_format=None,
        missing_worksheet_action=GetDataFromFormMissingWorksheetAction.RAISE_EXCEPTION
    )

Inputs
------

Pass:

* `guide_filename` - filename of the guide spreadsheet
* `in_filename` - filename of the input spreadsheet
* `date_format` - if None, any date formatted cells in the spreadsheet will be returned as Python datetime.datetime objects.
  If set, they will be turned into strings using strftime.
  For format options, see `Python docs <https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes>`_ .
* `missing_worksheet_action` - what to do if the guide spreadsheet specifies a worksheet that does not exist in the input spreadsheet.

Possible options for `missing_worksheet_action` are:

* `GetDataFromFormMissingWorksheetAction.RAISE_EXCEPTION` - raise an exception of class `spreadsheetforms.exceptions.MissingWorksheetException`
* `GetDataFromFormMissingWorksheetAction.SET_NO_DATA` - silently ignores the problem. The data keys that should have been set from the missing worksheet will just not exist in the output.

Outputs
-------

Returns a JSON representation of the data extracted from the form.
