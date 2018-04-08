from django.shortcuts import render, HttpResponse, redirect



def create(request):

    response = "Hello, I am your test"
    return HttpResponse(response)
    # if request.method == "POST":
    #     print "*"*50
    #     print request.POST
    # print request.POST['name']
    # print request.POST['desc']
    # request.session['name'] = "test"
    #     print "*"*50
    #     return redirect("/")
    # else:
    #     return redirect("/")