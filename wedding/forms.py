from django import forms


class GuestsForm(forms.Form):
    names = forms.CharField(label="Names", max_length=100)
    is_attending = forms.BooleanField(required=False)
    number_of_guests = forms.IntegerField(min_value=0, max_value=9)
    meal = forms.CharField(max_length=100)
    song_1 = forms.CharField(max_length=100)
    song_2 = forms.CharField(max_length=100)
    song_3 = forms.CharField(max_length=100)
