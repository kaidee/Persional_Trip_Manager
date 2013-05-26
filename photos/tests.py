"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from models import Photo, Gallery



class ViewsBaseCase(TestCase):
	fixtures = ['photo.json']

class PhotoTest(ViewsBaseCase):
	"""docstring for PostTest"""
	# def setUp(self):
		# self.client = Client

	def test_new(self):
		#not login
		resp = self.client.get(reverse('photo_gallery_index'))
		self.assertEqual(resp.status_code, 302)
		#login
		assert self.client.login(username='user', password='user')
		resp = self.client.get(reverse('photo_gallery_index'))
		self.assertEqual(resp.status_code, 200)