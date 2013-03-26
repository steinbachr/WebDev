from django import forms

class UserForm(forms.Form):  
    name = forms.CharField(max_length=80, widget=forms.HiddenInput())
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
    public = forms.BooleanField(widget=forms.CheckboxInput(), initial=True, required=False)
    player_cap = forms.IntegerField(max_value=50, widget=forms.TextInput(), required=False)
    start_date = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'datepicker'}))
    start_time = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder' : 'e.g. 3:45PM'}))
    player_names = forms.CharField(max_length=500, widget=forms.HiddenInput(), required=False)
    player_ids = forms.CharField(max_length=500, widget=forms.HiddenInput(), required=False)
