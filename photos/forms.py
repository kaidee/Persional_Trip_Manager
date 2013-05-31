# coding:utf-8
# Author:kaidee

from django import forms
# from django.db import IntegrityError

from photos.models import *

class PhotoForm(forms.Form):
	title = forms.CharField(label='标题', 
		max_length=100, widget=forms.TextInput(attrs={'placeholder': '请输入标题（非必填）'}), required=False)
	description	= forms.CharField(label='内容', 
		widget=forms.Textarea(attrs={'placeholder': '请输入内容（非必填）'}), required=False)
	image = forms.ImageField(label='图片', required=False)

class GalleryForm(forms.ModelForm):

	class Meta:
		model = Gallery
		fields = ['title', 'description']

	def save(self, owner=None):
		if not self.instance.pk:
			self.instance.owner = owner
		gallery = super(GalleryForm, self).save()
		return gallery