from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


  # the index function is called when root is visited
def index(request):                         #localhost:8000/
    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }
    return render(request, "first_app/index.html", context)


def test(request):                          #localhost:8000/first_app/test
    response = "Hello, I am your test"
    return HttpResponse(response)