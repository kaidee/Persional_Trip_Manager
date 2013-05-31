# coding:utf-8
# Author:kaidee

from django import forms

from models import Post, Plan

from bootstrap.forms import BootstrapModelForm

class PostForm(BootstrapModelForm):

	class Meta:
		model = Post
		fields = ['title', 'content']

	def clean_content(self):
		content = self.cleaned_data.get('content', '')
		num_words = len(content)
		if num_words < 4:
			raise forms.ValidationError("字数不够！")
		return content
	def save(self, owner=None):
		if not self.instance.pk:
			self.instance.owner = owner
		post = super(PostForm, self).save()
		return post

class PlanForm(forms.Form):
	content = forms.CharField(label='', 
		widget=forms.Textarea(attrs={'placeholder': '内容'}), required=True)