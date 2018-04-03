================================
Global Login Required Middleware
================================

This module is a Django middleware that make all views and URLs login required.


-----------

.. contents::

-----------


Documentation
-------------

Usage
_____
To install this app, you should add ``'global_login_required.LoginRequiredMiddleware'`` to ``settings.MIDDLEWARE``

.. code-block::python
    MIDDLEWARE = [
        # default contents
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        ...

        'global_login_required.LoginRequiredMiddleware',
    ]

then all routes in your sile will be login required.

there is 3 ways to exclude a route from being login required:

- Add a ``@login_not_required`` decorator for view function
- List the public view (not login required views) in settings.py at ``PUBLIC_VIEWS``
- List the public route's regex is settings.py at ``PUBLIC_PATHS``

.. danger::
    The ``login_not_required`` decorator currently is only for **function based view**.
    for using it with **class based views** should be by `Decorating in URLconf`_:

    .. code-block:: python
        
        from global_login_required import login_not_required
        
        urlpatterns = [
        ....
            path(r'^cbv_decorator/', login_not_required(test_ClassBasedView_decorator.as_view())),
        ....
        ]

.. danger::
    The ``login_not_required`` decorator actually do nothing and only wrap the view in an object and we check for object type, So:

    - If you combine this decorator with a ``login_required`` decorator, your view will be login required.
    - Make shure that this decorator is the last one that applies on a view.

    This will fix in next versions.

.. _Decorating in URLconf: https://docs.djangoproject.com/en/dev/topics/class-based-views/intro/#decorating-in-urlconf


Settings
________
There is 2 settings available

PUBLIC_VIEWS
************
This setting is a **python list** that contains string path to any view that you want to make it publicly available:

.. code-block:: python

    PUBLIC_VIEWS = [
        'django.contrib.auth.views.login',
        'myapp.views.the_view',
    ]

The middleware will check every request and if responsible view of the request was listed at this setting,
it will ignore checking for authentication.

.. note::
    The view listed here can be **function based** or **class based**.


PUBLIC_PATHS
************
This setting is a **python list** that contains regex strings of URIs that you to make them publicly available:


.. code-block:: python

    PUBLIC_PATHS = [
        '^%s.*' % MEDIA_URL, # allow public access to any media on your application
        r'^/accounts/.*', # allow public access to all django-allauth views
    ]

the ``r`` letter before the regular expression is **optional** and tells python that this is a regex not a normal python string,
but python ``re`` package can handel this itself.

also you can list exact URL in here.

The middleware will check every request and if URI of the request match with any of listed regular expressions,
it will ignore checking for authentication.


.. warning::
    It's important to handel authentication of urls that are private but match with some of listed patterns.

    For example user profile page (``/accounts/profile/``) in above example should be login required:

    - You can use ``login_required`` decorator for such views.
    - You can write more complex regex that ensures correct access rights.



.. note::
    If you manually add a ``login_required`` decorator to view, and then list that view in settings,
    the final final result will be **login required**.

Code Documentation
__________________

.. automodule:: global_login_required
    :members:
    :undoc-members:
    :show-inheritance:
