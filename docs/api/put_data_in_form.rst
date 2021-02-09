put_data_in_form function
=========================

Purpose
-------

Populates a spreadsheet form with existing JSON data, based on the structure of a guide form.

Call
----

.. code-block:: python

    from spreadsheetforms.api import put_data_in_form

    put_data_in_form(guide_filename, data, out_filename)

Inputs
------

Pass:

* guide_filename - filename of the guide spreadsheet
* data - a JSON block of the data
* out_filename - filename of the output spreadsheet

Outputs
-------

Returns nothing; simply creates or replaces the out_filename file.
