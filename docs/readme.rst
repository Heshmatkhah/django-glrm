=======================================
Django Global Login Required Middleware
=======================================

This module is a Django middleware that make all views and URLs login required.


-----------

.. contents::

-----------


Documentation
-------------

Installation
____________
you can install Django Global Login Required Middleware using ``pip``::

    $ pip install django-glrm


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

        ...
    ]

then all routes in your sile will be login required.

there is 4 ways to exclude a url or view from being login required:

- Add a ``@login_not_required`` decorator for view (**function based** or **class based**)
- List the public view (not login required views) in settings.py at PUBLIC_VIEWS_
- List the public url's regex is settings.py at PUBLIC_PATHS_
- Add ``LOGIN_NOT_REQUIRED`` property to view class

Decorator
_________
if you want to use ``login_not_required`` decorator for a **class based view**, it should be in one of this formats:

1. Use as a normal decorator for class

.. code-block:: python

    from global_login_required import login_not_required
    from django.views.generic import ListView

    @login_not_required
    class test_ClassBasedView_decorator(ListView):
        ...

2. `Decorating in URLconf`_:

.. code-block:: python

    from global_login_required import login_not_required

    urlpatterns = [
    ...
        path(r'^cbv_decorator/', login_not_required(test_ClassBasedView_decorator.as_view())),
    ...
    ]

3. `Decorating the class`_:

.. code-block:: python

    from global_login_required import login_not_required
    from django.utils.decorators import method_decorator
    from django.views.generic import ListView

    @method_decorator(login_not_required, name='dispatch')
    class test_ClassBasedView_method_decorator(ListView):
        ...


.. _Decorating in URLconf: https://docs.djangoproject.com/en/dev/topics/class-based-views/intro/#decorating-in-urlconf
.. _Decorating the class: https://docs.djangoproject.com/en/dev/topics/class-based-views/intro/#decorating-the-class

.. danger::
    If you combine ``login_not_required`` decorator with a ``login_required`` decorator, your view will be login required.

Class Property
______________
also you can a ``LOGIN_NOT_REQUIRED`` to your class based views and your class will be publicly available:

.. code-block:: python

    from django.views.generic import ListView

    class test_ClassBasedView_property_public(ListView):
        LOGIN_NOT_REQUIRED = True # Makes the view publicly available

        def get(self, request, *args, **kwargs):
            return HttpResponse("Response from view.")


If you set ``LOGIN_NOT_REQUIRED`` to ``False`` your view still login required:

.. code-block:: python

    from django.views.generic import ListView

    class test_ClassBasedView_property(ListView):
        LOGIN_NOT_REQUIRED = False # The view still login required

        def get(self, request, *args, **kwargs):
            return HttpResponse("Response from view.")


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

