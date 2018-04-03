from django.contrib.auth.decorators import login_required
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
import re


class GlobalLoginRequiredMiddleware(MiddlewareMixin):
	"""
	Main idea from `Julien Phalip <https://www.julienphalip.com/blog/site-wide-login-protection-and-public-views/>`_

	.. note::
		Compatible with django 1.11+
	"""

	def __init__(self, get_response=None):
		"""
		initialize the middleware:

		- populate `public_patterns` from settings's `PUBLIC_VIEWS` (list) if exists
		- populate `public_views` from settings's `PUBLIC_PATHS` (list of regex) if exists

		:param get_response: the actual view or the next middleware in the chain. provided by django middleware system.
		"""
		super(GlobalLoginRequiredMiddleware, self).__init__(get_response)
		self.public_patterns = []
		self.public_views = []
		if hasattr(settings, 'PUBLIC_VIEWS'):
			for view_path in settings.PUBLIC_VIEWS:
				view = self.get_view(view_path)
				self.public_views.append(view)
		if hasattr(settings, 'PUBLIC_PATHS'):
			for public_path in settings.PUBLIC_PATHS:
				self.public_patterns.append(re.compile(public_path))

	def get_view(self, view_path):
		"""
		returns callable instance of view from view path
		:param view_path: view path, like `'django.contrib.auth.views.login'`
		:return: a callable instance of view, in this example `login`
		"""
		i = view_path.rfind('.')
		module_path, view_name = view_path[:i], view_path[i + 1:]
		module = __import__(module_path, globals(), locals(), [view_name])
		return getattr(module, view_name)

	def matches_public_view(self, view):
		"""
		Checks is the view is listed in `PUBLIC_VIEWS`, so it is not login required.

		:param callable view: the view
		:return: true if view was listed in `PUBLIC_VIEWS`.
		:rtype: bool
		"""
		if self.public_views:
			if hasattr(view, 'view_class'):
				if view.view_class in self.public_views:
					return True

			if view in self.public_views:
				return True

		return False

	def matches_public_path(self, path):
		"""
		Checks is the request path is listed in `PUBLIC_PATHS`, so it is not login required.

		:param string path: the request path
		:return: true if view was listed in `PUBLIC_PATHS`.
		:rtype: bool
		"""
		if self.public_patterns:
			for pattern in self.public_patterns:
				if pattern.match(path) is not None:
					return True
		return False

	def process_view(self, request, view_func, view_args, view_kwargs):
		"""
		checks if this view is not in excluded views (by `PUBLIC_VIEWS`, `PUBLIC_PATHS` or `login_not_required` decorator),
		adds `login_required` decorator for view, otherwise run the view it self.

		.. note::
			read the documentation at `djangoproject <https://docs.djangoproject.com/en/1.11/topics/http/middleware/#process-view>`_

		:param HttpRequest request: this will be passed to next process_view and finally will be passed to view.
		:param callable view_func: the view function
		:param view_args: the arguments that will be passed to view
		:param view_kwargs: the keyword arguments that will be passed to view
		:return: `None` in order to  continue processing **process_view** in middleware chain or ` HttpResponse` for braking middleware chain.
		"""
		if request.user.is_authenticated() or isinstance(view_func, login_not_required) or self.matches_public_path(request.path) or self.matches_public_view(view_func):
			return None
		else:
			return login_required(view_func)(request, *view_args, **view_kwargs)


# todo: make this compatible with Class Based Views
class login_not_required(object):
	"""
	Decorator which marks the given view as public (no login required).

	This class actually do nothing, but it wrap view in an object and we can use
	``isinstance`` to detect that function is not a login required one.		

	So if you combine this with a ``login_required`` decorator, your view will be login required.
	Also make shure that this decorator is the last one that apply on a view.
	
	This will fix in next versions.

	"""

	def __init__(self, original_function):
		"""
		Set the function in the class
		:param callable original_function: the function
		"""
		self.original_function = original_function

	def __call__(self, *args, **kwargs):
		"""
		calls the function

		:param args:
		:param kwargs:
		:return: function's output
		"""
		return self.original_function(*args, **kwargs)
