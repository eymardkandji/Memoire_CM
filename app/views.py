from django.shortcuts import render
from django.shortcuts import HttpResponse
from proxmoxer import ProxmoxAPI as pveAPI
from django.http import JsonResponse

nodes_name = []
nodes_state = []
cluster_name = ''
cluster_logs1 = []
cluster_logs2 = []
cluster_tasks = []
nodes_vms = []


def api():
    # host = '37.187.77.208'
    # password = "KimtfuZV1hcFlOlm"
    host = "192.168.168.100"
    password = "pveroot"
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
    global nodes_name, nodes_state, cluster_name, cluster_logs1, cluster_logs2, cluster_tasks

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

    cluster_logs = pve.cluster.log.get(max=11)
    cluster_logs1 = cluster_logs[:5]
    cluster_logs2 = cluster_logs[5:]

    def sort_tasks_by_starttime(tasks):
        return sorted(tasks, key=lambda x: x['starttime'])

    cluster_tasks = pve.cluster.tasks.get()
    cluster_tasks = sort_tasks_by_starttime(cluster_tasks)
    cluster_tasks = cluster_tasks[-8:]


def update_node():
    global nodes_vms
    nodes_vms = []
    pve = api()
    for node in pve.nodes.get():
        if node['status'] == 'online':
            qemu = []
            lxc = []
            node_name = node['node']
            for vm in pve.nodes(node_name).qemu.get():
                vm_i = vm
                vm_i["qemu_conf"] = pve.nodes(node_name).qemu(vm['vmid']).config.get()
                qemu.append(vm_i)
            for lx in pve.nodes(node_name).lxc.get():
                lx_i = lx
                lx_i["lxc_conf"] = pve.nodes(node_name).lxc(lx['vmid']).config.get()
                lxc.append(lx_i)
            node_i = {
                "node": node,
                "qemu": qemu,
                "lxc": lxc
            }
        else:
            node_i = {
                "node": node,
                "qemu": None,
                "lxc": None
            }
        nodes_vms.append(node_i)
    print(nodes_vms)


def base(request):
    updated()
    return render(request, "web/base.html", context={
        "cluster_name": cluster_name
    })


def index(request):
    updated()
    write_dash()
    return render(request, "web/index.html", context={
        "cluster_name": cluster_name,
        "nodes_state": nodes_state,
        "cluster_logs1": cluster_logs1,
        "cluster_logs2": cluster_logs2,
        "cluster_tasks": cluster_tasks
    })


def netwoks(request):
    return render(request, "web/networks.html", context={
        "cluster_name": cluster_name,
    })


def nodes(request):
    update_node()
    return render(request, "web/nodes.html", context={
        "cluster_name": cluster_name,
        "node_vms": nodes_vms
    })


def high_a(request):
    return render(request, "web/high_a.html", context={
        "cluster_name": cluster_name,
    })


def update_chart_data(request):
    global nodes_state
    updated()
    data = {}
    for node in nodes_state:
        if node['status'] == 'online':
            lg = node['loadavg']
            lg = [float(value) for value in lg]
            data[node['node']] = {
                'memory': [node['memory']['used'], node['memory']['free']],
                'disk': [node['rootfs']['used'], node['rootfs']['free']],
                'cpu': [node['cpu'], 1 - node['cpu']],
                'swap': [node['swap']['used'], node['swap']['free']],
                'load': lg
            }
    return JsonResponse(data)


def write_dash():
    def generate_node_script(node, id):
        node_name = node['node']
        return f"""
        document.addEventListener("DOMContentLoaded", function() {{
            var ctxMemory_{id} = document.getElementById("pie-chart-{node_name}-memory").getContext("2d");
            var ctxDisk_{id} = document.getElementById("pie-chart-{node_name}-disk").getContext("2d");
            var ctxCpu_{id} = document.getElementById("pie-chart-{node_name}-cpu").getContext("2d");
            var ctxSwap_{id} = document.getElementById("pie-chart-{node_name}-swap").getContext("2d");

            var backgroundColor = ["rgb(158,227,190)", "rgba(64,69,83,0.88)"];
            var options = {{
                responsive: true,
                plugins: {{
                    legend: {{
                        position: 'bottom'
                    }},
                    datalabels: {{
                        formatter: (value, context) => {{
                            let total = context.dataset.data.reduce((a, b) => a + b, 0);
                            let percentage = (value / total * 100).toFixed(1) + "%";
                            return percentage;
                        }},
                        color: '#fff',
                        labels: {{
                            title: {{
                                font: {{
                                    weight: 'bold'
                                }}
                            }}
                        }}
                    }}
                }}
            }};

            var chartMemory_{id} = new Chart(ctxMemory_{id}, {{
                type: "pie",
                data: {{ labels: ["Use", "Free"], datasets: [{{ backgroundColor, data: [0, 0] }}] }},
                options,
                plugins: [ChartDataLabels]
            }});
            var chartDisk_{id} = new Chart(ctxDisk_{id}, {{
                type: "pie",
                data: {{ labels: ["Use", "Free"], datasets: [{{ backgroundColor, data: [0, 0] }}] }},
                options,
                plugins: [ChartDataLabels]
            }});
            var chartCpu_{id} = new Chart(ctxCpu_{id}, {{
                type: "pie",
                data: {{ labels: ["Use", "Free"], datasets: [{{ backgroundColor, data: [0, 0] }}] }},
                options,
                plugins: [ChartDataLabels]
            }});
            var chartSwap_{id} = new Chart(ctxSwap_{id}, {{
                type: "pie",
                data: {{ labels: ["Use", "Free"], datasets: [{{ backgroundColor, data: [0, 0] }}] }},
                options,
                plugins: [ChartDataLabels]
            }});

            // Function to update charts with new data
            function updateCharts(data) {{
                chartMemory_{id}.data.datasets[0].data = data['{node_name}'].memory;
                chartMemory_{id}.update();

                chartDisk_{id}.data.datasets[0].data = data['{node_name}'].disk;
                chartDisk_{id}.update();

                chartCpu_{id}.data.datasets[0].data = data['{node_name}'].cpu;
                chartCpu_{id}.update();

                chartSwap_{id}.data.datasets[0].data = data['{node_name}'].swap;
                chartSwap_{id}.update();

                $('.pg-bar').waypoint(function () {{
                    $('.progress #pg-bar-{node_name}-1').each(function () {{
                        var val = (data['{node_name}'].load[0] * 100) / 3.5;
                        $(this).css('width', val.toFixed(2) + '%');
                        $(this).text(val.toFixed(2) + '% ---- ' + data['{node_name}'].load[0]+ ' ---- 1min');
                    }});
                }}, {{ offset: '80%' }});
                $('.pg-bar').waypoint(function () {{
                    $('.progress #pg-bar-{node_name}-5').each(function () {{
                        var val = (data['{node_name}'].load[1] * 100) / 3.5;
                        $(this).css('width', val.toFixed(2) + '%');
                        $(this).text(val.toFixed(2) + '% ---- ' + data['{node_name}'].load[1] + ' ---- 5min');
                    }});
                }}, {{ offset: '80%' }});
                $('.pg-bar').waypoint(function () {{
                    $('.progress #pg-bar-{node_name}-10').each(function () {{
                        var val = (data['{node_name}'].load[2] * 100) / 3.5;
                        $(this).css('width', val.toFixed(2) + '%');
                        $(this).text(val.toFixed(2) + '% ---- ' + data['{node_name}'].load[2]+ ' ---- 10min');
                    }});
                }}, {{ offset: '80%' }});
            }}

            // Listen for HTMX updates
            document.body.addEventListener('htmx:afterOnLoad', (event) => {{
                // Assumes new JSON data is in event.detail.xhr.response
                if (event.detail.target.id === 'chart-content') {{
                    let newData = JSON.parse(event.detail.xhr.response);
                    updateCharts(newData);
                }}
            }});

            $('.pg-bar').waypoint(function () {{
                $('.progress .progress-bar').each(function () {{
                    var val = $(this).attr("aria-valuenow") * 100;
                    $(this).css("width",  val + '%');
                }});
            }}, {{ offset: '80%' }});
        }});
        """

    global nodes_state
    updated()
    with open('app/static/web/js/dash.js', 'w') as fichier:
        id = 0
        for node in nodes_state:
            id += 1
            if node['status'] == 'online':
                fichier.write(generate_node_script(node, id))
    return HttpResponse("Updating OK")

