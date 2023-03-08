fetch("datajson.json").then(function (response) {
    return response.json();
})
    .then(function (data) {
        appendData(data);
    })
    .catch(function (err) {
        console.log('error:' + err);
    })

function appendData(data) {
    let mainContainer = document.getElementById("weatherData");


    var div = document.createElement("div");
    div.innerHTML = `weather ${data.temp_f}`;
    mainContainer.appendChild(div);

}