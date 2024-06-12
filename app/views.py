from django.shortcuts import render

from proxmoxer import ProxmoxAPI as pveAPI


# Create your views here.
def base(request):

    host = "192.168.168.100"
    userid = "root@pam"
    password = "node1"
    ssl = False
    pve = pveAPI(
        host,
        user=userid,
        password=password,
        verify_ssl=ssl
    )
    nodes_name = []
    for _ in pve.cluster.status.get():
        if _['type'] == 'node':
            nodes_name.append(_['name'])
        else:
            cluster_name = _['name']
    return render(request, "web/base.html", context={
        "nodes_name": nodes_name,
        "cluster_name": cluster_name
    })


def index(request):
    return render(request, "web/index.html")


def netwok(request):
    return render(request, "web/network.html")
