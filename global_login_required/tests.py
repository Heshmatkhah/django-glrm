from django.test import TestCase, override_settings, modify_settings
from django.contrib.auth.models import User
from django.conf import settings


@modify_settings(MIDDLEWARE={
	'append': 'global_login_required.GlobalLoginRequiredMiddleware',
})
@override_settings(ROOT_URLCONF='global_login_required.urls')
class LoginRequired_Test(TestCase):

	def setUp(self):
		self.testuser = User.objects.create_user(username='testuser', password='123456')

	@modify_settings(PUBLIC_VIEWS={
		'prepend': 'global_login_required.views.test_ClassBasedView',
	})
	def test_settings_class_based_view(self):
		# Not logged in

		# test cbv, no parameter in url
		response = self.client.get('/cbv/')
		self.assertEqual(response.status_code, 200)

		# test cbv, parameter in url
		response = self.client.get('/cbv_with_param/12/abc/')
		self.assertEqual(response.status_code, 200)

		# Login
		self.client.force_login(self.testuser)

		# test cbv, no parameter in url
		response = self.client.get('/cbv/')
		self.assertEqual(response.status_code, 200)

		# test cbv, parameter in url
		response = self.client.get('/cbv_with_param/12/abc/')
		self.assertEqual(response.status_code, 200)

	@modify_settings(PUBLIC_VIEWS={
		'prepend': 'global_login_required.views.test_FunctionBasedView',
	})
	def test_settings_function_based_view(self):
		# Not logged in

		# test fbv, no parameter in url
		response = self.client.get('/fbv/')
		self.assertEqual(response.status_code, 200)

		# test fbv, parameter in url
		response = self.client.get('/fbv_with_param/12/abc/')
		self.assertEqual(response.status_code, 200)

		# Login
		self.client.force_login(self.testuser)

		# test fbv, no parameter in url
		response = self.client.get('/fbv/')
		self.assertEqual(response.status_code, 200)

		# test fbv, parameter in url
		response = self.client.get('/fbv_with_param/12/abc/')
		self.assertEqual(response.status_code, 200)

	@modify_settings(PUBLIC_PATHS={
		'prepend': '/cbv(_with_param)?/.*',
	})
	def test_settings_url_regex_class_based_view(self):
		# Not logged in

		# test cbv, no parameter in url
		response = self.client.get('/cbv/')
		self.assertEqual(response.status_code, 200)

		# test cbv, parameter in url
		response = self.client.get('/cbv_with_param/12/abc/')
		self.assertEqual(response.status_code, 200)

		# Login
		self.client.force_login(self.testuser)

		# test cbv, no parameter in url
		response = self.client.get('/cbv/')
		self.assertEqual(response.status_code, 200)

		# test cbv, parameter in url
		response = self.client.get('/cbv_with_param/12/abc/')
		self.assertEqual(response.status_code, 200)

	@modify_settings(PUBLIC_PATHS={
		'prepend': '/fbv(_with_param)?/.*',
	})
	def test_settings_url_regex_function_based_view(self):
		# Not logged in

		# test fbv, no parameter in url
		response = self.client.get('/fbv/')
		self.assertEqual(response.status_code, 200)

		# test fbv, parameter in url
		response = self.client.get('/fbv_with_param/12/abc/')
		self.assertEqual(response.status_code, 200)

		# Login
		self.client.force_login(self.testuser)

		# test fbv, no parameter in url
		response = self.client.get('/fbv/')
		self.assertEqual(response.status_code, 200)

		# test fbv, parameter in url
		response = self.client.get('/fbv_with_param/12/abc/')
		self.assertEqual(response.status_code, 200)

	def test_decorator_class_based_view(self):
		# Not logged in

		# test cbv, no parameter in url
		response = self.client.get('/cbv_url_decorator/')
		self.assertEqual(response.status_code, 200)

		# test cbv, parameter in url
		response = self.client.get('/cbv_with_param_url_decorator/12/abc/')
		self.assertEqual(response.status_code, 200)

		# test cbv, no parameter in url
		response = self.client.get('/cbv_decorator/')
		self.assertEqual(response.status_code, 200)

		# test cbv, parameter in url
		response = self.client.get('/cbv_with_param_decorator/12/abc/')
		self.assertEqual(response.status_code, 200)

		# test cbv, no parameter in url
		response = self.client.get('/cbv_method_decorator/')
		self.assertEqual(response.status_code, 200)

		# test cbv, parameter in url
		response = self.client.get('/cbv_with_param_method_decorator/12/abc/')
		self.assertEqual(response.status_code, 200)

		# Login
		self.client.force_login(self.testuser)

		# test cbv, no parameter in url
		response = self.client.get('/cbv_url_decorator/')
		self.assertEqual(response.status_code, 200)

		# test cbv, parameter in url
		response = self.client.get('/cbv_with_param_url_decorator/12/abc/')
		self.assertEqual(response.status_code, 200)

		# test cbv, no parameter in url
		response = self.client.get('/cbv_decorator/')
		self.assertEqual(response.status_code, 200)

		# test cbv, parameter in url
		response = self.client.get('/cbv_with_param_decorator/12/abc/')
		self.assertEqual(response.status_code, 200)

		# test cbv, no parameter in url
		response = self.client.get('/cbv_method_decorator/')
		self.assertEqual(response.status_code, 200)

		# test cbv, parameter in url
		response = self.client.get('/cbv_with_param_method_decorator/12/abc/')
		self.assertEqual(response.status_code, 200)

	def test_decorator_function_based_view(self):
		# Not logged in

		# test fbv, no parameter in url
		response = self.client.get('/fbv_decorator/')
		self.assertEqual(response.status_code, 200)

		# test fbv, parameter in url
		response = self.client.get('/fbv_with_param_decorator/12/abc/')
		self.assertEqual(response.status_code, 200)

		# Login
		self.client.force_login(self.testuser)

		# test fbv, no parameter in url
		response = self.client.get('/fbv_decorator/')
		self.assertEqual(response.status_code, 200)

		# test fbv, parameter in url
		response = self.client.get('/fbv_with_param_decorator/12/abc/')
		self.assertEqual(response.status_code, 200)

	def test_normal_page(self):
		# Not logged in

		# test cbv, no parameter in url
		response = self.client.get('/cbv/')
		self.assertRedirects(response, settings.LOGIN_URL + '?next=/cbv/')

		# test cbv, parameter in url
		response = self.client.get('/cbv_with_param/12/abc/')
		self.assertRedirects(response, settings.LOGIN_URL + '?next=/cbv_with_param/12/abc/')

		# test fbv, no parameter in url
		response = self.client.get('/fbv/')
		self.assertRedirects(response, settings.LOGIN_URL + '?next=/fbv/')

		# test fbv, parameter in url
		response = self.client.get('/fbv_with_param/12/abc/')
		self.assertRedirects(response, settings.LOGIN_URL + '?next=/fbv_with_param/12/abc/')

		# Login
		self.client.force_login(self.testuser)

		# test cbv, no parameter in url
		response = self.client.get('/cbv/')
		self.assertEqual(response.status_code, 200)

		# test cbv, parameter in url
		response = self.client.get('/cbv_with_param/12/abc/')
		self.assertEqual(response.status_code, 200)

		# test fbv, no parameter in url
		response = self.client.get('/fbv/')
		self.assertEqual(response.status_code, 200)

		# test fbv, parameter in url
		response = self.client.get('/fbv_with_param/12/abc/')
		self.assertEqual(response.status_code, 200)

	def test_property_class_based_view(self):
		# Not logged in

		# test cbv, no parameter in url
		response = self.client.get('/cbv_property/')
		self.assertRedirects(response, settings.LOGIN_URL + '?next=/cbv_property/')

		# test cbv, parameter in url
		response = self.client.get('/cbv_with_param_property/12/abc/')
		self.assertRedirects(response, settings.LOGIN_URL + '?next=/cbv_with_param_property/12/abc/')

		# test cbv, no parameter in url
		response = self.client.get('/cbv_property_public/')
		self.assertEqual(response.status_code, 200)

		# test cbv, parameter in url
		response = self.client.get('/cbv_with_param_property_public/12/abc/')
		self.assertEqual(response.status_code, 200)

		# Login
		self.client.force_login(self.testuser)

		# test cbv, no parameter in url
		response = self.client.get('/cbv_property/')
		self.assertEqual(response.status_code, 200)

		# test cbv, parameter in url
		response = self.client.get('/cbv_with_param_property/12/abc/')
		self.assertEqual(response.status_code, 200)

		# test cbv, no parameter in url
		response = self.client.get('/cbv_property_public/')
		self.assertEqual(response.status_code, 200)

		# test cbv, parameter in url
		response = self.client.get('/cbv_with_param_property_public/12/abc/')
		self.assertEqual(response.status_code, 200)
