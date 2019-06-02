import json
from django.shortcuts import render


# Create your views here.
def cv(request, json_file="cv/static/FMu.json"):
    with open(json_file, 'r') as file:
        json_data = json.load(file)
    response = render(request,
                      "cv/cv.html", {'data': json_data})
    return response
