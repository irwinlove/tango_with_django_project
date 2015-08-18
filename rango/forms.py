from django import forms
from rango.models import Page,Category

class CategoryForm(forms.ModelForm):
	"""docstring for CategoryForm"""
	name = forms.CharField(max_length=128, help_text="Please enter the category name.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)
	class Meta:
		"""docstring for Meta"""
		model =Category
		fields =('name',)
class PageForm(forms.ModelForm):
	"""docstring for PageForm"""
	title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
	url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	class Meta:
		"""docstring for Meta"""
		model = Page
		exclude = ('category',)
	# def clean(self):
	# 	cleaned_data = self.cleaned_data
	# 	url = cleaned_data.get('url')
	# 	if url and not url.startswith('http://'):
	# 		url = 'http://'+url
	# 		cleaned_data['url'] = url
	# 		pass
	# 	return cleaned_data
		

		
		