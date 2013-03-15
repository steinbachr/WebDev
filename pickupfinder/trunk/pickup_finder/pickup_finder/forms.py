from django import forms

class UserForm(forms.Form):  
    name = forms.CharField(max_length=50, widget=forms.HiddenInput())
    fb_id = forms.CharField(max_length=50, widget=forms.HiddenInput())
    
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        name = cleaned_data.get('name', None)
        fb_id = cleaned_data.get('fb_id', None)
        
        #if name or fb_id is null, we've hit a problem
        if name is None or fb_id is None:
            raise forms.ValidationError("hit a problem processing request")
        
        return cleaned_data
    
    
class GameForm(forms.Form):
    location = forms.CharField(max_length=50)
    public = forms.BooleanField(widget=forms.CheckboxInput())
    player_cap = forms.IntegerField(max_value=50, required=False, widget=forms.TextInput(attrs={'disabled' : True}))
    start = forms.DateTimeField()
