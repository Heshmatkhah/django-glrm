from django.utils.decorators import method_decorator

from django.views.generic import TemplateView
from django.http import HttpResponse
from . import login_not_required


def test_FunctionBasedView(request, **kwargs):
	return HttpResponse("Response from view.")


class test_ClassBasedView(TemplateView):
	template_name = 'test.html'


@login_not_required
def test_FunctionBasedView_decorator(request, **kwargs):
	return HttpResponse("Response from view.")


class test_ClassBasedView_decorator(TemplateView):
	template_name = 'test.html'
