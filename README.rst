=============================================
Global Login Required Middleware |Doc_Badge|_
=============================================

This module is a Django middleware that make all views and URLs login required.

`Detailed documentation <http://djnago-glrm.readthedocs.io/>`_ is in the "docs" directory.

-----------

.. contents::

-----------


Quick start
-----------

1. Add "global_login_required.GlobalLoginRequiredMiddleware" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'global_login_required.GlobalLoginRequiredMiddleware',
    ]

2. Start the development server and visit http://127.0.0.1:8000/, 
now all your pages are login required and you will see the login page.

.. |Doc_Badge| image:: https://readthedocs.org/projects/djnago-glrm/badge/?version=latest
.. _Doc_Badge: http://djnago-glrm.readthedocs.io/