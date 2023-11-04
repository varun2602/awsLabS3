from django.db import models

class ImageUpload(models.Model):
    image_upload = models.ImageField(upload_to="images/")
    date_upload = models.DateTimeField(auto_now_add=True)

