import uuid

from django.db import models

from click_and_collect.models import ClickCollectLocations


class UpcomingShows(models.Model):
    artist_name = models.CharField(max_length=100)
    artist_image = models.ImageField(
        default='default.jpg', upload_to='shows_images')
    venue = models.ForeignKey(ClickCollectLocations, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f'{self.artist_name} @ {self.venue}'


class ShowsTickets(models.Model):
    custom_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    artist = models.ForeignKey(UpcomingShows, on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=40, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.artist} | {self.ticket_type}'
