from django.db import models


class Guests(models.Model):
    names = models.TextField()
    is_attending = models.BooleanField(default=None, null=False)
    attending_standesamt = models.BooleanField(default=None, null=False)
    attending_party = models.BooleanField(default=None, null=False)
    meal = models.TextField(blank=True)
    song_1 = models.TextField(blank=True)
    song_2 = models.TextField(blank=True)
    song_3 = models.TextField(blank=True)

    @property
    def name(self):
        return str(self.names)

    @property
    def unique_id(self):
        return str(self.pk)

    def __str__(self):
        return "Party: {} {}".format(self.names, self.is_attending)
