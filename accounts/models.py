"""Models.py files."""
# Standard Library
from datetime import date

# Django
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models

# 3rd-party
from dateutil.relativedelta import relativedelta
from multiselectfield import MultiSelectField
from PIL import Image

# Local
from .consts import categories
from .consts import sex_category


class CustomUser(AbstractUser):  # noqa D101
    email = models.EmailField(max_length=254)
    premium = models.BooleanField(
        blank=True,
        default=False,
    )
    city = models.CharField(max_length=100)
    birth_date = models.DateField(blank=True, null=True)

    descriptions = models.TextField(blank=True)
    sex = models.CharField(max_length=150, choices=sex_category)

    class Meta:  # noqa: D106
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):  # noqa: D105
        today = date.today()
        age = relativedelta(today, self.birth_date)

        return f'{self.email} {self.last_name} {age.years}'


class PhotoUser(models.Model):  # noqa D101
    date_add = models.DateField()
    photo = models.ImageField(upload_to='photo', null=True, blank=True)
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:  # noqa: D106

        verbose_name = 'Photo User'
        verbose_name_plural = 'Photo Users'

    def save(self, *args, **kwargs):  # noqa D102
        super().save(*args, **kwargs)
        img = Image.open(self.photo.path)

        if img.height > 600 or img.width > 500:
            output_size = (600, 500)
            img.thumbnail(output_size)
            img.save(self.photo.path)

    def __str__(self):  # noqa: D105
        return f'{self.custom_user.first_name} {self.custom_user.last_name} {self.photo}'


class Preferences(models.Model):  # noqa D101

    age_min = models.IntegerField(
        default=18,
        validators=[
            MaxValueValidator(200),
            MinValueValidator(18),
        ],
    )

    age_max = models.IntegerField(
        default=18,
        validators=[
            MaxValueValidator(200),
            MinValueValidator(18),
        ],
    )

    tags = MultiSelectField(choices=categories)
    sex = models.CharField(max_length=150, choices=sex_category)
    custom_user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )

    class Meta:  # noqa: D106

        verbose_name = 'Preference'
        verbose_name_plural = 'Preferences'

    def __str__(self):  # noqa D105
        return f'{self.tags} {self.age_min} {self.age_max} {self.sex}'
