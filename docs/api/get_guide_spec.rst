get_guide_spec function
=======================

Purpose
-------

Extracts a JSON representation of the structure of a spreadsheet form specified in a guide form.

You can use this in combination with :doc:`get_data_from_form_with_guide_spec<get_data_from_form_with_guide_spec>`
if :doc:`get_data_from_form<get_data_from_form>` is to slow.

Call
----

.. code-block:: python

    from spreadsheetforms.api import get_guide_spec

    data = get_guide_spec(guide_filename):


Inputs
------

Pass:

* guide_filename - filename of the guide spreadsheet


Outputs
-------

Returns a JSON representation of the structure specified in the guide form.

