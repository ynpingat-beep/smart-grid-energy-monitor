// ================= Dashboard Summary =================

function loadDashboard() {

    fetch("/dashboard/summary")
        .then(response => response.json())
        .then(data => {

            document.getElementById("sensors").innerHTML = data.total_sensors;

            document.getElementById("active").innerHTML = data.active_sensors;

            document.getElementById("readings").innerHTML = data.total_readings;

            document.getElementById("voltage").innerHTML =
                data.average_voltage + " V";

            document.getElementById("energy").innerHTML =
                data.total_energy + " kWh";

        });

}

loadDashboard();


// ================= Recent Sensors =================

function loadSensors() {

    fetch("/dashboard/recent")
        .then(response => response.json())
        .then(data => {

            let rows = "";

            data.forEach(sensor => {

                let badge = "";

                if (sensor.status === "Active") {

                    badge =
                        `<span class="status active">🟢 Active</span>`;

                } else {

                    badge =
                        `<span class="status inactive">🔴 Offline</span>`;

                }

                rows += `

                <tr>

                    <td>${sensor.id}</td>

                    <td>${sensor.sensor_name}</td>

                    <td>${sensor.location}</td>

                    <td>${badge}</td>

                    <td>Just Now</td>

                </tr>

                `;

            });

            document.getElementById("sensorTable").innerHTML = rows;

        });

}

loadSensors();


// ================= Live Clock =================

function updateClock() {

    const now = new Date();

    const options = {
        weekday: "short",
        day: "2-digit",
        month: "short",
        year: "numeric",
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit"
    };

    document.getElementById("time").innerHTML =
        now.toLocaleString("en-IN", options);

}

updateClock();

setInterval(updateClock, 1000);


// ================= Voltage Chart =================

const voltageCtx = document.getElementById("voltageChart");

const voltageChart = new Chart(voltageCtx, {

    type: "line",

    data: {

        labels: [],

        datasets: [{

            label: "Voltage (V)",

            data: [],

            borderColor: "#2563eb",

            backgroundColor: "rgba(37,99,235,0.15)",

            borderWidth: 3,

            fill: true,

            tension: 0.4,

            pointRadius: 4,

            pointBackgroundColor: "#2563eb"

        }]

    },

    options: {

        responsive: true,

        plugins: {

            legend: {

                display: true

            }

        },

        scales: {

            y: {

                beginAtZero: false

            }

        }

    }

});


// ================= Power Chart =================

const powerCtx = document.getElementById("powerChart");

const powerChart = new Chart(powerCtx, {

    type: "bar",

    data: {

        labels: [],

        datasets: [{

            label: "Power (W)",

            data: [],

            backgroundColor: "#22c55e",

            borderRadius: 8

        }]

    },

    options: {

        responsive: true,

        plugins: {

            legend: {

                display: true

            }

        }

    }

});


// ================= Load Charts =================

function loadCharts() {

    fetch("/dashboard/chart")

        .then(response => response.json())

        .then(data => {

            const labels = data.map(item => "Reading " + item.id);

            const voltages = data.map(item => item.voltage);

            const powers = data.map(item => item.power);

            voltageChart.data.labels = labels;
            voltageChart.data.datasets[0].data = voltages;
            voltageChart.update();

            powerChart.data.labels = labels;
            powerChart.data.datasets[0].data = powers;
            powerChart.update();

        });

}

loadCharts();


// ================= Auto Refresh =================

setInterval(() => {

    loadDashboard();

    loadSensors();

    loadCharts();

}, 10000);