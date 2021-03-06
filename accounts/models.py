from django.db import models
from django.contrib.auth.models import User
# from phone_field import PhoneField
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default="default.png", upload_to="avatars")
    # contact_num = PhoneField(blank=True, help_text="Your contact number is secret.")

    def __str__(self):
        return f'{self.user.username}\'s profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.avatar.path)

        if img.width>300 and img.height>300:
            output=(300, 300)
            img.thumbnail(output)
            img.save(self.avatar.path)