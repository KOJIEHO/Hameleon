const form = document.getElementById('form')

function update_prodavec(){
    id = new URLSearchParams(window.location.search).get('idUser');
    fIO = document.form.Surname.value + " " + document.form.Name.value + " " + document.form.Middlename.value
    telefon = document.form.telefon.value
    prinyat = document.form.prinyat.value;
    dataRogdeniya = document.form.dataRogdeniya.value;
    
    data = [{
        "$id": id,
        "$type": "Prodavec",
        "FIO": fIO,
        "Telefon": telefon,
        "Prinyat": prinyat,
        "DataRogdeniya": dataRogdeniya,
    }]
    fetch("http://localhost:4388/ham/odata", {
        method: "PUT",
        body: JSON.stringify(data),
        headers: {
            "Content-type": "application/json"
        }
    })
        .then((response) => response.json())
        .then((json) => console.log(json));
}


function delete_prodavec(){
    id = new URLSearchParams(window.location.search).get('idUser');
    
    data = [{
        "$id": id,
        "$type": "Prodavec"
    }]
    fetch("http://localhost:4388/ham/odata/", { 
        method: "DELETE",
        body: JSON.stringify(data),
        headers: {
            "Content-type": "application/json"
        }
    })
}
