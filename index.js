document.addEventListener("DOMContentLoaded", function () {
    console.log("done");
    fetch('data.json')
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            appendData(data);
        })
        .catch(function (err) {
            console.log('error:' + err);
        })

    fetch('datajson.json')
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            appendData2(data);
        })
        .catch(function (err) {
            console.log('error:' + err);
        })
});


function appendData(data) {
    for (let productName in data) {
        for (let element of data[productName]) {

            let addThis = document.getElementById(element["productId"]);
            if (addThis == null) {
                addThis = document.createElement('div');
            }
            let image = document.createElement('img');
            image.src = element["location"];
            image.width = "300";
            image.height = "300";
            addThis.appendChild(image);

            let anotherElement = document.createElement('div');
            anotherElement.className += "card-body";
            addThis.appendChild(anotherElement);

            let header = document.createElement('h1');
            header.className += "display-5";
            header.innerHTML = element['playerName'];
            anotherElement.appendChild(header);

            let paragraph = document.createElement('p');
            paragraph.className += "lead";
            paragraph.innerHTML = "<br />" + element['description'];
            header.appendChild(paragraph);

            let randomDiv = document.createElement('div');
            randomDiv.className += "d-flex";
            randomDiv.className += "justify-content-between";
            randomDiv.className += "align-items-center";
            paragraph.appendChild(randomDiv);

            let price = document.createElement("small");
            price.className += "text-muted";
            price.innerHTML = "<br /><strong>$" + element["price"] + "</strong>";
            randomDiv.appendChild(price);



        }
    } // end of for
} // end of function appendData