from django import forms


class GuestsForm(forms.Form):
    names = forms.CharField(label="Names", max_length=100, required=True)
    is_attending = forms.BooleanField(required=False, initial=False)
    number_of_guests = forms.IntegerField(min_value=0, max_value=9, required=False)
    meal = forms.CharField(max_length=100, required=False)
    song_1 = forms.CharField(max_length=100, required=False)
    song_2 = forms.CharField(max_length=100, required=False)
    song_3 = forms.CharField(max_length=100, required=False)
