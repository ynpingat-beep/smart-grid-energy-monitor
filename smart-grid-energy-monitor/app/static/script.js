// ================= Dynamic Charts =================

const voltageCtx = document.getElementById("voltageChart");

const voltageChart = new Chart(voltageCtx, {

    type: "line",

    data: {

        labels: [],

        datasets: [{

            label: "Voltage (V)",

            data: [],

            borderColor: "#0d6efd",

            backgroundColor: "rgba(13,110,253,0.2)",

            fill: true,

            tension: 0.4

        }]

    }

});


const powerCtx = document.getElementById("powerChart");

const powerChart = new Chart(powerCtx, {

    type: "bar",

    data: {

        labels: [],

        datasets: [{

            label: "Power (W)",

            data: [],

            backgroundColor: "#198754"

        }]

    }

});


function loadCharts(){

fetch("/dashboard/chart")

.then(response=>response.json())

.then(data=>{

    const labels = data.map(item=>"Reading "+item.id);

    const voltages = data.map(item=>item.voltage);

    const powers = data.map(item=>item.power);

    voltageChart.data.labels = labels;
    voltageChart.data.datasets[0].data = voltages;
    voltageChart.update();

    powerChart.data.labels = labels;
    powerChart.data.datasets[0].data = powers;
    powerChart.update();

});

}

loadCharts();

setInterval(loadCharts,10000);