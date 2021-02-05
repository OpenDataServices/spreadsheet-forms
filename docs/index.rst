Spreadsheet Forms
=================

Spreadsheet Forms is a Python library for working with spreadsheets that contain data in forms.

If you create a form in a spreadsheet, it is easy to send to other people and ask them to fill it in and send it back to you.

However, it can then be hard for you to process. The worst case is you start extracting information out of these spreadsheets manually! This library attempts to solve that problem.

With the help of a Guide Form spreadsheet that tells the library how and where to work with data in the form, the library can:

* Extract data from the filled in spreadsheet into a JSON block of data. This is easy to store and process.
* Put existing data into a spreadsheet, so you can send that to someone and ask them to check existing data.
* Create a blank spreadsheet, so you can send that to someone and ask them to enter new data.

.. toctree::
   :maxdepth: 2

   examples.rst
   requirements.rst
   api/index.rst
   guideform/index.rst
