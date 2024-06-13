from django.shortcuts import render

from proxmoxer import ProxmoxAPI as pveAPI


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
print(nodes_name)
nodes_state = pve.nodes.get()

# Create your views here.
def base(request):

    return render(request, "web/base.html", context={
        "nodes_name": nodes_name,
        "cluster_name": cluster_name
    })


def index(request):
    return render(request, "web/index.html", context={
        "nodes_state": nodes_state,
        "nodes_name":nodes_name
    })


def netwok(request):
    return render(request, "web/network.html")
