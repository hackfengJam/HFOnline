================================================================================
pyexcel-io - Let you focus on data, instead of file formats
================================================================================

.. image:: https://raw.githubusercontent.com/pyexcel/pyexcel.github.io/master/images/patreon.png
   :target: https://www.patreon.com/pyexcel

.. image:: https://api.travis-ci.org/pyexcel/pyexcel-io.svg?branch=master
   :target: http://travis-ci.org/pyexcel/pyexcel-io

.. image:: https://codecov.io/gh/pyexcel/pyexcel-io/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/pyexcel/pyexcel-io

.. image:: https://img.shields.io/gitter/room/gitterHQ/gitter.svg
   :target: https://gitter.im/pyexcel/Lobby

.. image:: https://readthedocs.org/projects/pyexcel-io/badge/?version=latest
   :target: http://pyexcel-io.readthedocs.org/en/latest/

Support the project
================================================================================

If your company has embedded pyexcel and its components into a revenue generating
product, please `support me on patreon <https://www.patreon.com/bePatron?u=5537627>`_ to
maintain the project and develop it further.

If you are an individual, you are welcome to support me too on patreon and for however long
you feel like. As a patreon, you will receive
`early access to pyexcel related contents <https://www.patreon.com/pyexcel/posts>`_.

With your financial support, I will be able to invest
a little bit more time in coding, documentation and writing interesting posts.


Known constraints
==================

Fonts, colors and charts are not supported.

Introduction
================================================================================

**pyexcel-io** provides **one** application programming interface(API) to read
and write the data in excel format, import the data into and export the data
from database. It provides support for csv(z) format, django database and
sqlalchemy supported databases. Its supported file formats are extended to cover
"xls", "xlsx", "ods" by the following extensions:

.. _file-format-list:
.. _a-map-of-plugins-and-file-formats:

.. table:: A list of file formats supported by external plugins

   ======================== ======================= ================= ==================
   Package name              Supported file formats  Dependencies     Python versions
   ======================== ======================= ================= ==================
   `pyexcel-io`_            csv, csvz [#f1]_, tsv,                    2.6, 2.7, 3.3,
                            tsvz [#f2]_                               3.4, 3.5, 3.6
                                                                      pypy
   `pyexcel-xls`_           xls, xlsx(read only),   `xlrd`_,          same as above
                            xlsm(read only)         `xlwt`_
   `pyexcel-xlsx`_          xlsx                    `openpyxl`_       same as above
   `pyexcel-ods3`_          ods                     `pyexcel-ezodf`_, 2.6, 2.7, 3.3, 3.4
                                                    lxml              3.5, 3.6
   `pyexcel-ods`_           ods                     `odfpy`_          same as above
   ======================== ======================= ================= ==================

.. table:: Dedicated file reader and writers

   ======================== ======================= ================= ==================
   Package name              Supported file formats  Dependencies     Python versions
   ======================== ======================= ================= ==================
   `pyexcel-xlsxw`_         xlsx(write only)        `XlsxWriter`_     Python 2 and 3
   `pyexcel-odsr`_          read only for ods, fods lxml              same as above
   `pyexcel-htmlr`_         html(read only)         lxml,html5lib     same as above
   ======================== ======================= ================= ==================


.. _pyexcel-io: https://github.com/pyexcel/pyexcel-io
.. _pyexcel-xls: https://github.com/pyexcel/pyexcel-xls
.. _pyexcel-xlsx: https://github.com/pyexcel/pyexcel-xlsx
.. _pyexcel-ods: https://github.com/pyexcel/pyexcel-ods
.. _pyexcel-ods3: https://github.com/pyexcel/pyexcel-ods3
.. _pyexcel-odsr: https://github.com/pyexcel/pyexcel-odsr
.. _pyexcel-xlsxw: https://github.com/pyexcel/pyexcel-xlsxw
.. _pyexcel-htmlr: https://github.com/pyexcel/pyexcel-htmlr

.. _xlrd: https://github.com/python-excel/xlrd
.. _xlwt: https://github.com/python-excel/xlwt
.. _openpyxl: https://bitbucket.org/openpyxl/openpyxl
.. _XlsxWriter: https://github.com/jmcnamara/XlsxWriter
.. _pyexcel-ezodf: https://github.com/pyexcel/pyexcel-ezodf
.. _odfpy: https://github.com/eea/odfpy


In order to manage the list of plugins installed, you need to use pip to add or remove
a plugin. When you use virtualenv, you can have different plugins per virtual
environment. In the situation where you have multiple plugins that does the same thing
in your environment, you need to tell pyexcel which plugin to use per function call.
For example, pyexcel-ods and pyexcel-odsr, and you want to get_array to use pyexcel-odsr.
You need to append get_array(..., library='pyexcel-odsr').

.. rubric:: Footnotes

.. [#f1] zipped csv file
.. [#f2] zipped tsv file

If you need to manipulate the data, you might do it yourself or use its brother
library `pyexcel <https://github.com/pyexcel/pyexcel>`__ .

If you would like to extend it, you may use it to write your own
extension to handle a specific file format.




Installation
================================================================================

You can install pyexcel-io via pip:

.. code-block:: bash

    $ pip install pyexcel-io


or clone it and install it:

.. code-block:: bash

    $ git clone https://github.com/pyexcel/pyexcel-io.git
    $ cd pyexcel-io
    $ python setup.py install



Development guide
================================================================================

Development steps for code changes

#. git clone https://github.com/pyexcel/pyexcel-io.git
#. cd pyexcel-io

Upgrade your setup tools and pip. They are needed for development and testing only:

#. pip install --upgrade setuptools pip

Then install relevant development requirements:

#. pip install -r rnd_requirements.txt # if such a file exists
#. pip install -r requirements.txt
#. pip install -r tests/requirements.txt

Once you have finished your changes, please provide test case(s), relevant documentation
and update CHANGELOG.rst.

.. note::

    As to rnd_requirements.txt, usually, it is created when a dependent
    library is not released. Once the dependecy is installed
    (will be released), the future
    version of the dependency in the requirements.txt will be valid.


How to test your contribution
------------------------------

Although `nose` and `doctest` are both used in code testing, it is adviable that unit tests are put in tests. `doctest` is incorporated only to make sure the code examples in documentation remain valid across different development releases.

On Linux/Unix systems, please launch your tests like this::

    $ make

On Windows systems, please issue this command::

    > test.bat

How to update test environment and update documentation
---------------------------------------------------------

Additional steps are required:

#. pip install moban
#. git clone https://github.com/moremoban/setupmobans.git # generic setup
#. git clone https://github.com/pyexcel/pyexcel-commons.git commons
#. make your changes in `.moban.d` directory, then issue command `moban`

What is pyexcel-commons
---------------------------------

Many information that are shared across pyexcel projects, such as: this developer guide, license info, etc. are stored in `pyexcel-commons` project.

What is .moban.d
---------------------------------

`.moban.d` stores the specific meta data for the library.

Acceptance criteria
-------------------

#. Has Test cases written
#. Has all code lines tested
#. Passes all Travis CI builds
#. Has fair amount of documentation if your change is complex
#. Please update CHANGELOG.rst
#. Please add yourself to CONTRIBUTORS.rst
#. Agree on NEW BSD License for your contribution



License
================================================================================

New BSD License

Change log
================================================================================

0.5.4 - 10.11.2017
--------------------------------------------------------------------------------

updated
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#. PR `#44 <https://github.com/pyexcel/pyexcel-io/issues/44>`_, use unicodewriter
   for csvz writers.

0.5.3 - 23.10.2017
--------------------------------------------------------------------------------

updated
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#. pyexcel `#105 <https://github.com/pyexcel/pyexcel/issues/105>`_, remove gease
   from setup_requires, introduced by 0.5.2.
#. remove python2.6 test support

0.5.2 - 20.10.2017
--------------------------------------------------------------------------------

added
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#. `#103 <https://github.com/pyexcel/pyexcel/issues/103>`_, include LICENSE file
   in MANIFEST.in, meaning LICENSE file will appear in the released tar ball.

0.5.1 - 02.09.2017
--------------------------------------------------------------------------------

Fixed
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#. `pyexcel-ods issue 25<https://github.com/pyexcel/pyexcel-ods/issues/25>`_,
   Unwanted dependency on pyexcel. 

0.5.0 - 30.08.2017
--------------------------------------------------------------------------------

Added
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#. Collect all data type conversion codes as service.py.

Updated
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#. `#19 <https://github.com/pyexcel/pyexcel-io/issues/19>`_,
   use cString by default. For python, it will be a performance boost


0.4.4 - 08.08.2017
--------------------------------------------------------------------------------

Updated
********************************************************************************
#. `#42 <https://github.com/pyexcel/pyexcel-io/issues/42>`_, raise exception
   if database table name does not match the sheet name


0.4.3 - 29.07.2017
--------------------------------------------------------------------------------

Updated
********************************************************************************

#. `#41 <https://github.com/pyexcel/pyexcel-io/issues/41>`_, walk away gracefully
   when mmap is not available.

0.4.2 - 05.07.2017
--------------------------------------------------------------------------------

Updated
********************************************************************************

#. `#37 <https://github.com/pyexcel/pyexcel-io/issues/37>`_, permanently fix
   the residue folder pyexcel by release all future releases in a clean clone.


0.4.1 - 29.06.2017
--------------------------------------------------------------------------------

Updated
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#. `#39 <https://github.com/pyexcel/pyexcel-io/issues/39>`_, raise exception
   when bulk save in django fails. Please `bulk_save=False` if you as the
   developer choose to save the records one by one if bulk_save cannot be
   used. However, exception in one-by-one save case will be raised as well.
   This change is made to raise exception in the first place so that you as
   the developer will be suprised when it was deployed in production.

0.4.0 - 19.06.2017
--------------------------------------------------------------------------------

Updated
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#. 'built-in' as the value to the parameter 'library' as parameter to invoke
   pyexcel-io's built-in csv, tsv, csvz, tsvz, django and sql won't work.
   It is renamed to 'pyexcel-io'.
#. built-in csv, tsv, csvz, tsvz, django and sql are lazy loaded.
#. pyexcel-io plugin interface has been updated. v0.3.x plugins won't work.
#. `#32 <https://github.com/pyexcel/pyexcel-io/issues/32>`_, csv and csvz file
   handle are made sure to be closed. File close mechanism is enfored.
#. iget_data function is introduced to cope with dangling file handle issue.

Removed
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#. Removed plugin loading code and lml is used instead


0.3.4 - 18.05.2017
--------------------------------------------------------------------------------

Updated
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#. `#33 <https://github.com/pyexcel/pyexcel-io/issues/33>`_, handle mmap object
   differently given as file content. This issue has put in a priority to single
   sheet csv over multiple sheets in a single memory stream. The latter format
   is pyexcel own creation but is rarely used. In latter case,
   multiple_sheet=True should be passed along get_data.
#. `#34 <https://github.com/pyexcel/pyexcel-io/issues/34>`_, treat mmap object
   as a file content.
#. `#35 <https://github.com/pyexcel/pyexcel-io/issues/35>`_, encoding parameter
   take no effect when given along with file content
#. use ZIP_DEFALTED to really do the compression


0.3.3 - 30.03.2017
--------------------------------------------------------------------------------

Updated
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#. `#31 <https://github.com/pyexcel/pyexcel-io/issues/31>`_, support pyinstaller


0.3.2 - 26.01.2017
--------------------------------------------------------------------------------

Updated
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#. `#29 <https://github.com/pyexcel/pyexcel-io/issues/29>`_, change
   skip_empty_rows to False by default

0.3.1 - 21.01.2017
--------------------------------------------------------------------------------

Added
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#. updated versions of extra packages

Updated
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#. `#23 <https://github.com/pyexcel/pyexcel-io/issues/23>`_, provide helpful
   message when old pyexcel plugin exists
#. restored previously available diagnosis message for missing libraries


0.3.0 - 22.12.2016
--------------------------------------------------------------------------------

Added
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#. lazy loading of plugins. for example, pyexcel-xls is not entirely loaded
   until xls format is used at its first attempted reading or writing. Since
   it is loaded, it will not be loaded in the second io action.
#. `pyexcel-xls issue 11 <https://github.com/pyexcel/pyexcel-xls/issues/11>`_,
   make case-insensitive for file type


0.2.6 - 21.12.2016
--------------------------------------------------------------------------------

Updated
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#. `#24 <https://github.com/pyexcel/pyexcel-io/issues/24>`__, pass on batch_size


0.2.5 - 20.12.2016
--------------------------------------------------------------------------------

Updated
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#. `#26 <https://github.com/pyexcel/pyexcel-io/issues/26>`__, performance issue
   with getting the number of columns.

0.2.4 - 24.11.2016
--------------------------------------------------------------------------------

Updated
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#. `#23 <https://github.com/pyexcel/pyexcel-io/issues/23>`__, Failed to convert
   long integer string in python 2 to its actual value

0.2.3 - 16.09.2016
--------------------------------------------------------------------------------

Added
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#. `#21 <https://github.com/pyexcel/pyexcel-io/issues/21>`__, choose subset from
   data base tables for export
#. `#22 <https://github.com/pyexcel/pyexcel-io/issues/22>`__, custom renderer if
   given `row_renderer` as parameter.

0.2.2 - 31.08.2016
--------------------------------------------------------------------------------

Added
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#. support pagination. two pairs: start_row, row_limit and start_column,
   column_limit help you deal with large files.
#. `skip_empty_rows=True` was introduced. To include empty rows, put it to False.

Updated
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#. `#20 <https://github.com/pyexcel/pyexcel-io/issues/20>`__, pyexcel-io attempts
   to parse cell contents of 'infinity' as a float/int, crashes


0.2.1 - 11.07.2016
--------------------------------------------------------------------------------


Added
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#. csv format: handle utf-16 encoded csv files. Potentially being able to decode
   other formats if correct "encoding" is provided
#. csv format: write utf-16 encoded files. Potentially other encoding is also
   supported
#. support stdin as input stream and stdout as output stream

Updated
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#. Attention, user of pyexcel-io! No longer io stream validation is performed
   in python 3. The guideline is: io.StringIO for csv, tsv only, otherwise
   BytesIO for xlsx, xls, ods. You can use RWManager.get_io to produce a correct
   stream type for you.
#. `#15 <https://github.com/pyexcel/pyexcel-io/issues/15>`__, support foreign
   django/sql foreign key

0.2.0 - 01.06.2016
--------------------------------------------------------------------------------

Added
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#. autoload of pyexcel-io plugins
#. auto detect `datetime`, `float` and `int`. Detection can be switched off by
   `auto_detect_datetime`, `auto_detect_float`, `auto_detect_int`


0.1.0 - 17.01.2016
--------------------------------------------------------------------------------

Added
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# yield key word to return generator as content



