from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_image = models.ImageField(default='default.jpg', upload_to='profile_images')

	RED = 'red-scheme'
	BLUE = 'blue-scheme'
	GREEN = 'green-scheme'
	PINK = 'pink-scheme'
	PURPLE = 'purple-scheme'
	YELLOW = 'yellow-scheme'
	COLOR_SCHEME_CHOICES = [
		(RED, 'Red'),
		(BLUE, 'Blue'),
		(GREEN, 'Green'),
		(PINK, 'Pink'),
		(PURPLE, 'Purple'),
		(YELLOW, 'Yellow'),
	]
	color_scheme = models.CharField(
		max_length=13,
		choices=COLOR_SCHEME_CHOICES,
		default=RED,
	)

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		profile_image = Image.open(self.profile_image.path)

		if profile_image.height > 300 or profile_image.width > 300:
			target_size = (300, 300)
			profile_image.thumbnail(target_size)
			profile_image.save(self.profile_image.path)
