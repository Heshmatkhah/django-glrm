=============================================
Global Login Required Middleware |Doc_Badge|_
=============================================

Django Global Login Required Middleware (djnago-glrm) is a Django middleware that make all views and URLs login required.

It's common in Djnago that most of the site's pages are protected, with just a few exceptions of pages that remain public (e.g. login page, etc.).
It can be quite tedious to decorate all of the views with ``@login_required``, and it can be easy to forget to decorate some of them.

So, you can use **Django Global Login Required Middleware** to make all page login required excep some of them.

-----------

.. contents::

-----------


Quick start
-----------

1. Install Django Global Login Required Middleware::

    $ pip install djnago-global-login-required-middleware

2. Add "global_login_required.GlobalLoginRequiredMiddleware" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'global_login_required.GlobalLoginRequiredMiddleware',
    ]

3. Start the development server and visit http://127.0.0.1:8000/, 
now all your pages are login required and you will see the login page.

.. |Doc_Badge| image:: https://readthedocs.org/projects/djnago-glrm/badge/?version=latest
.. _Doc_Badge: http://djnago-glrm.readthedocs.io/