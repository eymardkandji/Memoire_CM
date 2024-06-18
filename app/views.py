from django.shortcuts import render

from proxmoxer import ProxmoxAPI as pveAPI

nodes_name = []
nodes_state = []
cluster_name = ''
cluster_logs = []
cluster_tasks = []


def api():
    # host = '37.187.77.208'
    # password = "KimtfuZV1hcFlOlm"
    host = "192.168.168.100"
    password = "node1"
    userid = "root@pam"
    ssl = False
    pve = pveAPI(
        host,
        user=userid,
        password=password,
        verify_ssl=ssl
    )
    return pve


def updated():

    global nodes_name, nodes_state, cluster_name, cluster_logs, cluster_tasks

    nodes_name = []
    pve = api()

    for _ in pve.cluster.status.get():
        if _['type'] == 'node':
            nodes_name.append(_['name'])
        else:
            cluster_name = _['name']

    nodes_state = []
    print(cluster_name)
    for _ in pve.nodes.get():

        node_ = {}

        if _["status"] == "online":
            node_ = pve.nodes(_['node']).status.get()
            node_['node'] = _["node"]
            node_['status'] = 'online'
        else:
            node_['node'] = _["node"]
            node_['status'] = 'offline'

        nodes_state.append(node_)

    cluster_logs = pve.cluster.log.get(max=10)
    cluster_tasks = pve.cluster.tasks.get()
    print(cluster_tasks)


def base(request):
    updated()
    return render(request, "web/base.html", context={
        "nodes_name": nodes_name,
        "cluster_name": cluster_name
    })


def index(request):
    updated()
    return render(request, "web/index.html", context={
        "cluster_name": cluster_name,
        "nodes_name": nodes_name,
        "nodes_state": nodes_state,
        "cluster_logs": cluster_logs,
        "cluster_tasks": cluster_tasks
    })


def netwok(request):
    return render(request, "web/network.html")
