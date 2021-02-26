from django.conf import settings
from django.db import models


# Create your models here.


def upload_location(instance, filename):
    return f'{instance.id}, {filename}'


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    image = models.ImageField(
        upload_to=upload_location,
        null=True,
        blank=True,
        width_field="width_field",
        height_field="height_field"
    )
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    content = models.TextField()
    update = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/posts/detail/{self.id}/'

