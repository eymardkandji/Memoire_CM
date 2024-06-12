from django.shortcuts import render


# Create your views here.
def base(request):
    nodes = {
        "nodes": ['Node 1', 'Node 2', 'Node 3']
    }
    return render(request, "web/base.html", context=nodes)

def netwok(request):
    return render(request, "web/network.html")
