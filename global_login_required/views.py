from django.views import View
from django.http import HttpResponse
from . import login_not_required
from django.utils.decorators import method_decorator


def test_FunctionBasedView(request, **kwargs):
	return HttpResponse("Response from view.")


class test_ClassBasedView(View):
	def get(self, request, *args, **kwargs):
		return HttpResponse("Response from view.")


@login_not_required
def test_FunctionBasedView_decorator(request, **kwargs):
	return HttpResponse("Response from view.")


class test_ClassBasedView_url_decorator(View):
	def get(self, request, *args, **kwargs):
		return HttpResponse("Response from view.")


@method_decorator(login_not_required, name='dispatch')
class test_ClassBasedView_method_decorator(View):
	def get(self, request, *args, **kwargs):
		return HttpResponse("Response from view.")


@login_not_required
class test_ClassBasedView_decorator(View):
	def get(self, request, *args, **kwargs):
		return HttpResponse("Response from view.")


class test_ClassBasedView_property(View):
	LOGIN_NOT_REQUIRED = False

	def get(self, request, *args, **kwargs):
		return HttpResponse("Response from view.")


class test_ClassBasedView_property_public(View):
	LOGIN_NOT_REQUIRED = True

	def get(self, request, *args, **kwargs):
		return HttpResponse("Response from view.")
