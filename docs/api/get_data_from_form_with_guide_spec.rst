get_data_from_form_with_guide_spec function
===========================================

Purpose
-------

This takes a spreadsheet with user entered data and returns the data the user entered.

This is a version of :doc:`get_data_from_form<get_data_from_form>` that should be used where performance is an issue.

:doc:`get_data_from_form<get_data_from_form>` will parse the guide spreadsheet every time it is called.
If called multiple times, or you need faster action when it is called, use this instead.
Call :doc:`get_guide_spec<get_guide_spec>` and cache the results. Pass that cached value to this function.

If performance is not an issue, we recommend just using :doc:`get_guide_spec<get_guide_spec>` as that is simpler.

Call
----

.. code-block:: python

    from spreadsheetforms.api import get_data_from_form_with_guide_spec

    data = get_data_from_form_with_guide_spec(
        guide_spec,
        in_filename,
        date_format=None
    )

Inputs
------

Pass:

* guide_spec - Data from calling the :doc:`get_guide_spec<get_guide_spec>` function
* in_filename - filename of the input spreadsheet
* date_format - if None, any date formatted cells in the spreadsheet will be returned as Python datetime.datetime objects.
  If set, they will be turned into strings using strftime.
  For format options, see `Python docs <https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes>`_ .

Outputs
-------

Returns a JSON block of the data it managed to extract from the input.