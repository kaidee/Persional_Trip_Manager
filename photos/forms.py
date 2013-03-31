# coding:utf-8
# Author:kaidee

from django import forms
from django.db import IntegrityError
from photos.models import *

class PhotoForm(forms.ModelForm):
	title = forms.CharField(label='标题', 
		max_length=100, widget=forms.TextInput(attrs={'placeholder': '请输入标题（非必填）'}))
	description	= forms.CharField(label='内容', 
		widget=forms.Textarea(attrs={'placeholder': '请输入内容（非必填）'}))
	# gallery	= forms.ModelMultipleChoiceField(label='相册', queryset=Gallery.objects.all())
	original = forms.ImageField(label='图片', required=False)
	# original = forms.ImageField(required=False)
	class Meta:
		model = Photo
		# exclude = ("owner")
	# class Meta:
	# 	model = Photo
	# 	fields =('title', 'description', 'gallery', 'original')
	# 	gallery		= forms.ModelMultipleChoiceField(queryset=Gallery.objects.all())
	# def save(self):
	# 	self.owner_id = '1'
	# 	return super(PhotoForm, self).save()