from django.shortcuts import render
import cv2
from . serializer import ImgSerializer
from django.http import JsonResponse
from .models import Img
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def img(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        two_cascade = cv2.CascadeClassifier('two.xml')
        four_cascade = cv2.CascadeClassifier('four.xml')
        img = cv2.imread(image)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        two = two_cascade.detectMultiScale(gray, 1.1, 1)
        two_count = len(two)
        four = four_cascade.detectMultiScale(gray, 1.1, 1)
        four_count = len(four)
        for (x, y, w, h) in two:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        for (x, y, w, h) in four:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow('img', img)
        cv2.waitKey(0)
        image = Img(image=img)
        image.save()
        return JsonResponse({'img': Img.objects.get(pk=image.id).image.url})
    return render(request, 'index.html')