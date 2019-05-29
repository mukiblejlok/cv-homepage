from django.shortcuts import render


# Create your views here.
def cv(request):
    response = render(request,
                      "cv/cv.html")
    return response
