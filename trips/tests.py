"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from models import Post, Plan



class ViewsBaseCase(TestCase):
	fixtures = ['testdata.json']

class PostTest(ViewsBaseCase):
	"""docstring for PostTest"""
	def setUp(self):
		self.client = Client

	def test_new(self):
		#not login
		resp = self.client.post(reverse('plan'))
		self.assertEqual(resp.status_code, 302)
	
