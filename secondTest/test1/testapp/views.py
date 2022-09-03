from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index (request):
#    data = {"header": "башка", "message": "месага"}
    return render(request, "index.html")    #, context= data)     #HttpResponse("<h0>МАША ATOMY луя витон <h0>")

#def about (request):
#    return HttpResponse("кукла")

#def contact (request):
#    return HttpResponse("бяка")y