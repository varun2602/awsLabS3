from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage


class PublicMediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False
    default_acl = 'public-read'

class ImageUpload(models.Model):
    image_upload = models.ImageField(storage= PublicMediaStorage() ,upload_to="images/")
    date_upload = models.DateTimeField(auto_now_add=True)

