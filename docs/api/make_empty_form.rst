make_empty_form function
========================

Purpose
-------

This takes a guide form and removes all special fields, creating a blank form that you can send to others to put data into.

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
