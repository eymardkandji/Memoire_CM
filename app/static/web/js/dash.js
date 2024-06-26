
        document.addEventListener("DOMContentLoaded", function() {
            var ctxMemory_1 = document.getElementById("pie-chart-PVE-1-memory").getContext("2d");
            var ctxDisk_1 = document.getElementById("pie-chart-PVE-1-disk").getContext("2d");
            var ctxCpu_1 = document.getElementById("pie-chart-PVE-1-cpu").getContext("2d");
            var ctxSwap_1 = document.getElementById("pie-chart-PVE-1-swap").getContext("2d");

            var backgroundColor = ["rgb(158,227,190)", "rgba(64,69,83,0.88)"];
            var options = {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'bottom'
                    },
                    datalabels: {
                        formatter: (value, context) => {
                            let total = context.dataset.data.reduce((a, b) => a + b, 0);
                            let percentage = (value / total * 100).toFixed(1) + "%";
                            return percentage;
                        },
                        color: '#fff',
                        labels: {
                            title: {
                                font: {
                                    weight: 'bold'
                                }
                            }
                        }
                    }
                }
            };

            var chartMemory_1 = new Chart(ctxMemory_1, {
                type: "pie",
                data: { labels: ["Use", "Free"], datasets: [{ backgroundColor, data: [0, 0] }] },
                options,
                plugins: [ChartDataLabels]
            });
            var chartDisk_1 = new Chart(ctxDisk_1, {
                type: "pie",
                data: { labels: ["Use", "Free"], datasets: [{ backgroundColor, data: [0, 0] }] },
                options,
                plugins: [ChartDataLabels]
            });
            var chartCpu_1 = new Chart(ctxCpu_1, {
                type: "pie",
                data: { labels: ["Use", "Free"], datasets: [{ backgroundColor, data: [0, 0] }] },
                options,
                plugins: [ChartDataLabels]
            });
            var chartSwap_1 = new Chart(ctxSwap_1, {
                type: "pie",
                data: { labels: ["Use", "Free"], datasets: [{ backgroundColor, data: [0, 0] }] },
                options,
                plugins: [ChartDataLabels]
            });

            // Function to update charts with new data
            function updateCharts(data) {
                chartMemory_1.data.datasets[0].data = data['PVE-1'].memory;
                chartMemory_1.update();

                chartDisk_1.data.datasets[0].data = data['PVE-1'].disk;
                chartDisk_1.update();

                chartCpu_1.data.datasets[0].data = data['PVE-1'].cpu;
                chartCpu_1.update();

                chartSwap_1.data.datasets[0].data = data['PVE-1'].swap;
                chartSwap_1.update();

                $('.pg-bar').waypoint(function () {
                    $('.progress #pg-bar-PVE-1-1').each(function () {
                        var val = (data['PVE-1'].load[0] * 100) / 3.5;
                        $(this).css('width', val.toFixed(2) + '%');
                        $(this).text(val.toFixed(2) + '% ---- ' + data['PVE-1'].load[0]+ ' ---- 1min');
                    });
                }, { offset: '80%' });
                $('.pg-bar').waypoint(function () {
                    $('.progress #pg-bar-PVE-1-5').each(function () {
                        var val = (data['PVE-1'].load[1] * 100) / 3.5;
                        $(this).css('width', val.toFixed(2) + '%');
                        $(this).text(val.toFixed(2) + '% ---- ' + data['PVE-1'].load[1] + ' ---- 5min');
                    });
                }, { offset: '80%' });
                $('.pg-bar').waypoint(function () {
                    $('.progress #pg-bar-PVE-1-10').each(function () {
                        var val = (data['PVE-1'].load[2] * 100) / 3.5;
                        $(this).css('width', val.toFixed(2) + '%');
                        $(this).text(val.toFixed(2) + '% ---- ' + data['PVE-1'].load[2]+ ' ---- 10min');
                    });
                }, { offset: '80%' });
            }

            // Listen for HTMX updates
            document.body.addEventListener('htmx:afterOnLoad', (event) => {
                // Assumes new JSON data is in event.detail.xhr.response
                if (event.detail.target.id === 'chart-content') {
                    let newData = JSON.parse(event.detail.xhr.response);
                    updateCharts(newData);
                }
            });

            $('.pg-bar').waypoint(function () {
                $('.progress .progress-bar').each(function () {
                    var val = $(this).attr("aria-valuenow") * 100;
                    $(this).css("width",  val + '%');
                });
            }, { offset: '80%' });
        });
        
        document.addEventListener("DOMContentLoaded", function() {
            var ctxMemory_3 = document.getElementById("pie-chart-PVE-0-memory").getContext("2d");
            var ctxDisk_3 = document.getElementById("pie-chart-PVE-0-disk").getContext("2d");
            var ctxCpu_3 = document.getElementById("pie-chart-PVE-0-cpu").getContext("2d");
            var ctxSwap_3 = document.getElementById("pie-chart-PVE-0-swap").getContext("2d");

            var backgroundColor = ["rgb(158,227,190)", "rgba(64,69,83,0.88)"];
            var options = {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'bottom'
                    },
                    datalabels: {
                        formatter: (value, context) => {
                            let total = context.dataset.data.reduce((a, b) => a + b, 0);
                            let percentage = (value / total * 100).toFixed(1) + "%";
                            return percentage;
                        },
                        color: '#fff',
                        labels: {
                            title: {
                                font: {
                                    weight: 'bold'
                                }
                            }
                        }
                    }
                }
            };

            var chartMemory_3 = new Chart(ctxMemory_3, {
                type: "pie",
                data: { labels: ["Use", "Free"], datasets: [{ backgroundColor, data: [0, 0] }] },
                options,
                plugins: [ChartDataLabels]
            });
            var chartDisk_3 = new Chart(ctxDisk_3, {
                type: "pie",
                data: { labels: ["Use", "Free"], datasets: [{ backgroundColor, data: [0, 0] }] },
                options,
                plugins: [ChartDataLabels]
            });
            var chartCpu_3 = new Chart(ctxCpu_3, {
                type: "pie",
                data: { labels: ["Use", "Free"], datasets: [{ backgroundColor, data: [0, 0] }] },
                options,
                plugins: [ChartDataLabels]
            });
            var chartSwap_3 = new Chart(ctxSwap_3, {
                type: "pie",
                data: { labels: ["Use", "Free"], datasets: [{ backgroundColor, data: [0, 0] }] },
                options,
                plugins: [ChartDataLabels]
            });

            // Function to update charts with new data
            function updateCharts(data) {
                chartMemory_3.data.datasets[0].data = data['PVE-0'].memory;
                chartMemory_3.update();

                chartDisk_3.data.datasets[0].data = data['PVE-0'].disk;
                chartDisk_3.update();

                chartCpu_3.data.datasets[0].data = data['PVE-0'].cpu;
                chartCpu_3.update();

                chartSwap_3.data.datasets[0].data = data['PVE-0'].swap;
                chartSwap_3.update();

                $('.pg-bar').waypoint(function () {
                    $('.progress #pg-bar-PVE-0-1').each(function () {
                        var val = (data['PVE-0'].load[0] * 100) / 3.5;
                        $(this).css('width', val.toFixed(2) + '%');
                        $(this).text(val.toFixed(2) + '% ---- ' + data['PVE-0'].load[0]+ ' ---- 1min');
                    });
                }, { offset: '80%' });
                $('.pg-bar').waypoint(function () {
                    $('.progress #pg-bar-PVE-0-5').each(function () {
                        var val = (data['PVE-0'].load[1] * 100) / 3.5;
                        $(this).css('width', val.toFixed(2) + '%');
                        $(this).text(val.toFixed(2) + '% ---- ' + data['PVE-0'].load[1] + ' ---- 5min');
                    });
                }, { offset: '80%' });
                $('.pg-bar').waypoint(function () {
                    $('.progress #pg-bar-PVE-0-10').each(function () {
                        var val = (data['PVE-0'].load[2] * 100) / 3.5;
                        $(this).css('width', val.toFixed(2) + '%');
                        $(this).text(val.toFixed(2) + '% ---- ' + data['PVE-0'].load[2]+ ' ---- 10min');
                    });
                }, { offset: '80%' });
            }

            // Listen for HTMX updates
            document.body.addEventListener('htmx:afterOnLoad', (event) => {
                // Assumes new JSON data is in event.detail.xhr.response
                if (event.detail.target.id === 'chart-content') {
                    let newData = JSON.parse(event.detail.xhr.response);
                    updateCharts(newData);
                }
            });

            $('.pg-bar').waypoint(function () {
                $('.progress .progress-bar').each(function () {
                    var val = $(this).attr("aria-valuenow") * 100;
                    $(this).css("width",  val + '%');
                });
            }, { offset: '80%' });
        });
        