function ChartModule_base(series, canvas_width, canvas_height,pos_top,pos_left,tt) {
    // Create the tag:
    var canvas_tag = "<canvas width='" + canvas_width + " !important' height='" + canvas_height + "!important' ";
    canvas_tag += "style='border: 3px solid black;position: relative; left:" + pos_left +"px; top:" + pos_top +"px;'></canvas>";
    // Append it to #elements
    var canvas = $(canvas_tag)[0];
    $("#elements").append(canvas);
    // Create the context and the drawing controller:
    var context = canvas.getContext("2d");
    var convertColorOpacity = function(hex) {

        if (hex.indexOf('#') != 0) {
            return 'rgba(0,0,0,0.1)';
        }

        hex = hex.replace('#', '');
        r = parseInt(hex.substring(0, 2), 16);
        g = parseInt(hex.substring(2, 4), 16);
        b = parseInt(hex.substring(4, 6), 16);
        return 'rgba(' + r + ',' + g + ',' + b + ',0.1)';
    };

    // Prep the chart properties and series:
    var datasets = []
    for (var i in series) {
        var s = series[i];
        var new_series = {
            label: s.Label,
            borderColor: s.Color,
            backgroundColor: convertColorOpacity(s.Color),
            data: []
        };
        datasets.push(new_series);
    }

    var chartData = {
        labels: [],
        datasets: datasets
    };

    var chartOptions = {
        responsive: true,
        tooltips: {
            mode: 'index',
            intersect: false
        },
		title: {
			display: true,
			text: tt
		},
        hover: {
            mode: 'nearest',
            intersect: true
        },
        scales: {
            xAxes: [{
                display: true,
                scaleLabel: {
                    display: true
                },
                ticks: {
                    maxTicksLimit: 11
                }
            }],
            yAxes: [{
                display: true,
                scaleLabel: {
                    display: true
                }
            }]
        }
    };

	// Creating the chart
    var chart = new Chart(context, {
        type: 'line',
        data: chartData,
        options: chartOptions
    });
	
	// Render chart with updated data
    this.render = function(data) {
        chart.data.labels.push(control.tick);
        for (i = 0; i < data.length; i++) {
            chart.data.datasets[i].data.push(data[i]);
        }
        chart.update();
    };

	// Reset chart
    this.reset = function() {
        while (chart.data.labels.length) { chart.data.labels.pop(); }
        chart.data.datasets.forEach(function(dataset) {
            while (dataset.data.length) { dataset.data.pop(); }
        });
        chart.update();
    };
};
