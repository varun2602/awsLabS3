from django.shortcuts import render, HttpResponse 
from . import models

def index(request):
    if request.method == "GET":
        images_all = models.ImageUpload.objects.all()
        context = {"all_images":images_all}
        return render(request, "index.html", context)
    if request.method == "POST":
        image_to_upload = request.FILES.get("image")
        image_model = models.ImageUpload.objects.create(image_upload = image_to_upload)
        image_model.save()
        
        return render(request, "index.html")
