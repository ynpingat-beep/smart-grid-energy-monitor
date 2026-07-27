// ================= Dashboard Summary =================

function loadDashboard(){

fetch("/dashboard/summary")
.then(response=>response.json())
.then(data=>{

document.getElementById("sensors").innerHTML=data.total_sensors;

document.getElementById("active").innerHTML=data.active_sensors;

document.getElementById("readings").innerHTML=data.total_readings;

document.getElementById("voltage").innerHTML=data.average_voltage+" V";

document.getElementById("energy").innerHTML=data.total_energy+" kWh";

});

}

loadDashboard();


// ================= Recent Sensors =================

function loadSensors(){

fetch("/dashboard/recent")
.then(response=>response.json())
.then(data=>{

let rows="";

data.forEach(sensor=>{

let badge="";

if(sensor.status=="Active"){

badge="<span class='active'>🟢 Active</span>";

}

else{

badge="<span class='inactive'>🔴 Inactive</span>";

}

rows+=`

<tr>

<td>${sensor.id}</td>

<td>${sensor.sensor_name}</td>

<td>${badge}</td>

<td>${sensor.location}</td>

</tr>

`;

});

document.getElementById("sensorTable").innerHTML=rows;

});

}

loadSensors();


// ================= Live Time =================

function updateClock(){

let now=new Date();

document.getElementById("time").innerHTML=
now.toLocaleString();

}

updateClock();

setInterval(updateClock,1000);


// ================= Auto Refresh =================

setInterval(()=>{

loadDashboard();

loadSensors();

},10000);

// ---------------- Voltage Chart ----------------

const voltageCtx = document.getElementById("voltageChart");

new Chart(voltageCtx, {

    type: "line",

    data: {

        labels: ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],

        datasets: [{

            label: "Voltage (V)",

            data: [228,230,229,231,230,232,231],

            borderColor: "#0d6efd",

            backgroundColor: "rgba(13,110,253,0.2)",

            tension: 0.4,

            fill: true

        }]

    }

});


// ---------------- Power Chart ----------------

const powerCtx = document.getElementById("powerChart");

new Chart(powerCtx, {

    type: "bar",

    data: {

        labels: ["Zone A","Zone B","Zone C","Zone D"],

        datasets: [{

            label: "Power (kW)",

            data: [120,95,150,110],

            backgroundColor: [

                "#0d6efd",

                "#198754",

                "#fd7e14",

                "#dc3545"

            ]

        }]

    }

});