from django import forms

class SearchForm(forms.Form):
    '''the form for searching for a pickup game'''
    location = forms.CharField(max_length=200)
