# coding:utf-8
# Author:kaidee

from django import forms

class PostForm(forms.Form):
	title = forms.CharField(label='',max_length=150, 
		required=True, widget=forms.TextInput(attrs={'placeholder': '标题'}))
	content = forms.CharField(label='', 
		widget=forms.Textarea(attrs={'placeholder': '内容'}), required=True)

	def clean_content(self):
		content = self.cleaned_data.get('content', '')
		num_words = len(content)
		if num_words < 4:
			raise forms.ValidationError("字数不够！")
		return content

class PlanForm(forms.Form):
	content = forms.CharField(label='', 
		widget=forms.Textarea(attrs={'placeholder': '内容'}), required=True)