from django.conf.urls import url, include
from .views import *
from . import login_not_required

urlpatterns = [
	url(r'^accounts/', include('allauth.urls')),
	url(r'^cbv_with_param/(?P<p1>.*)/(?P<p2>.*)/', test_ClassBasedView.as_view()),
	url(r'^cbv/', test_ClassBasedView.as_view()),
	url(r'^fbv_with_param/(?P<p1>.*)/(?P<p2>.*)/', test_FunctionBasedView),
	url(r'^fbv/', test_FunctionBasedView),
	url(r'^cbv_with_param_decorator/(?P<p1>.*)/(?P<p2>.*)/', test_ClassBasedView_decorator.as_view()),
	url(r'^cbv_decorator/', test_ClassBasedView_decorator.as_view()),
	url(r'^cbv_with_param_method_decorator/(?P<p1>.*)/(?P<p2>.*)/', test_ClassBasedView_method_decorator.as_view()),
	url(r'^cbv_method_decorator/', test_ClassBasedView_method_decorator.as_view()),
	url(r'^cbv_with_param_url_decorator/(?P<p1>.*)/(?P<p2>.*)/', login_not_required(test_ClassBasedView_url_decorator.as_view())),
	url(r'^cbv_url_decorator/', login_not_required(test_ClassBasedView_url_decorator.as_view())),
	url(r'^fbv_with_param_decorator/(?P<p1>.*)/(?P<p2>.*)/', test_FunctionBasedView_decorator),
	url(r'^fbv_decorator/', test_FunctionBasedView_decorator),
	url(r'^cbv_with_param_property/(?P<p1>.*)/(?P<p2>.*)/', test_ClassBasedView_property.as_view()),
	url(r'^cbv_property/', test_ClassBasedView_property.as_view()),
	url(r'^cbv_with_param_property_public/(?P<p1>.*)/(?P<p2>.*)/', test_ClassBasedView_property_public.as_view()),
	url(r'^cbv_property_public/', test_ClassBasedView_property_public.as_view()),
]
