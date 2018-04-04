.. Django Global Login Required Middleware documentation master file, created by
   sphinx-quickstart on Tue Apr  3 17:25:09 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Django Global Login Required Middleware's documentation!
===================================================================

Django Global Login Required Middleware (django-glrm) is a Django middleware that make all views and URLs login required.

It's common in Django that most of the site's pages are protected, with just a few exceptions of pages that remain public (e.g. login page, etc.).
It can be quite tedious to decorate all of the views with ``@login_required``, and it can be easy to forget to decorate some of them.

So, you can use **Django Global Login Required Middleware** to make all page login required excep some of them.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   readme
   code

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
