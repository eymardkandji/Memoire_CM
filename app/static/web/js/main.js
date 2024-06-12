(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Sidebar Toggler
    $('.sidebar-toggler').click(function () {
        $('.sidebar, .content').toggleClass("open");
        return false;
    });

    // Calender
    $('#calender').datetimepicker({
        inline: true,
        format: 'L'
    });

    // Pie Chart
    var ctx1 = $("#pie-chart-memory").get(0).getContext("2d");
    var myChart1 = new Chart(ctx1, {
        type: "pie",
        data: {
            labels: ["Free", "Use"],
            datasets: [{
                backgroundColor: [
                    "rgba(234,220,220,0.7)",
                    "rgba(235, 22, 22, .7)"
                ],
                data: [15, 85]
            }]
        },
        options: {
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
    },
    plugins: [ChartDataLabels]
});
    var ctx2 = $("#pie-chart-disk").get(0).getContext("2d");
    var myChart2 = new Chart(ctx2, {
        type: "pie",
        data: {
            labels: ["Free", "Use"],
            datasets: [{
                backgroundColor: [
                    "rgba(234,220,220,0.7)",
                    "rgba(235, 22, 22, .7)"
                ],
                data: [15, 85]
            }]
        },
        options: {
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
    },
    plugins: [ChartDataLabels]
});
    var ctx3 = $("#pie-chart-cpu").get(0).getContext("2d");
    var myChart3 = new Chart(ctx3, {
        type: "pie",
        data: {
            labels: ["Free", "Use"],
            datasets: [{
                backgroundColor: [
                    "rgba(234,220,220,0.7)",
                    "rgba(235, 22, 22, .7)"
                ],
                data: [15, 85]
            }]
        },
        options: {
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
    },
    plugins: [ChartDataLabels]
});

    var ctx4 = $("#pie-chart-swap").get(0).getContext("2d");
    var myChart4 = new Chart(ctx4, {
        type: "pie",
        data: {
            labels: ["Free", "Use"],
            datasets: [{
                backgroundColor: [
                    "rgba(234,220,220,0.7)",
                    "rgba(235, 22, 22, .7)"
                ],
                data: [15, 85]
            }]
        },
        options: {
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
    },
    plugins: [ChartDataLabels]
});

    
})(jQuery);

