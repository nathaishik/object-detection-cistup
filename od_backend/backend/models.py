from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
def img_path(instance, filename):
    return 'images/{0}'.format(filename + '_' + uuid.uuid4())


class Img(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to=img_path, blank=False)
