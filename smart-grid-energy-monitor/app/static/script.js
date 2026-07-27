fetch("/dashboard/summary")

.then(response=>response.json())

.then(data=>{

document.getElementById("sensors").innerHTML=data.total_sensors;

document.getElementById("readings").innerHTML=data.total_readings;

document.getElementById("voltage").innerHTML=data.average_voltage+" V";

});