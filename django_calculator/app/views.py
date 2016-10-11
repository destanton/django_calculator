from django.shortcuts import render


def index_view(request):
    print(request.POST)
    
    return render(request, "index.html")
