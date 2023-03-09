from django.shortcuts import render,redirect

# Create your views here.

def index(request):
    if request.method == "POST":
        content = request.POST.get("content",'')

        if content:
            print('Content :',content)
            return redirect ('index')

    return render(request, "post/index.html")