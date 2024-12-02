const form = document.getElementById('form')

function klient_update(){
    id = new URLSearchParams(window.location.search).get('idUser');
    fIO = document.form.Surname.value + " " + document.form.Name.value + " " + document.form.Middlename.value
    pasport = document.form.seria.value + " " + document.form.nomer.value
    organizacia = document.form.organizacia.value;
    telefon = document.form.telefon.value;
    
    data = [{
        "$id": id,
        "$type": "Klient",
        "FIO": fIO,
        "Pasport": pasport,
        "Organizaciya": organizacia,
        "Telefon": telefon,
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


function klient_delete(){
    id = new URLSearchParams(window.location.search).get('idUser');

    data = [{
        "$id": id,
        "$type": "Klient"
    }]
    fetch("http://localhost:4388/ham/odata/", { 
        method: "DELETE",
        body: JSON.stringify(data),
        headers: {
            "Content-type": "application/json"
        }
    })
}
