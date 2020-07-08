get_guide_spec function
=======================

This takes a guide spreadsheet and returns the specification of the spreadsheet as a JSON block.

You can use this in combination with :doc:`get_data_from_form_with_guide_spec<get_data_from_form_with_guide_spec>`
if :doc:`get_data_from_form<get_data_from_form>` is to slow.

.. code-block:: python

    get_guide_spec(guide_filename):


Pass:

* guide_filename - filename of the guide spreadsheet

Returns:

* data - a JSON block of the specification for the guide form
