make_empty_form function
========================

Purpose
-------

Generates a blank spreadsheet form based on the structure specified in a guide form.

Call
----

.. code-block:: python

    from spreadsheetforms.api import make_empty_form

    make_empty_form(guide_filename, out_filename):


Inputs
------

Pass:

* guide_filename - filename of the guide spreadsheet
* out_filename - filename of the output spreadsheet

Outputs
-------

Returns nothing; simply creates or replaces the out_filename file.
