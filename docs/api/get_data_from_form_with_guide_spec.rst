get_data_from_form_with_guide_spec function
===========================================

Purpose
-------

Extracts JSON data from a spreadsheet form, based on a structure specified in JSON.

This is a version of :doc:`get_data_from_form<get_data_from_form>` that should be used where performance is an issue.

:doc:`get_data_from_form<get_data_from_form>` will parse the guide spreadsheet every time it is called.
If called multiple times, or you need faster action when it is called, use this instead.
Call :doc:`get_guide_spec<get_guide_spec>` and cache the results. Pass that cached value to this function.

If performance is not an issue, we recommend just using :doc:`get_guide_spec<get_guide_spec>` as that is simpler.

Call
----

.. code-block:: python

    from spreadsheetforms.api import get_data_from_form_with_guide_spec, GetDataFromFormMissingWorksheetAction

    data = get_data_from_form_with_guide_spec(
        guide_spec,
        in_filename,
        date_format=None,
        missing_worksheet_action=GetDataFromFormMissingWorksheetAction.RAISE_EXCEPTION
    )

Inputs
------

Pass:

* guide_spec - Data from calling the :doc:`get_guide_spec<get_guide_spec>` function

Other parameters are the same as specified for :doc:`get_data_from_form<get_data_from_form>`.

Outputs
-------

Returns a JSON block of the data it managed to extract from the input.