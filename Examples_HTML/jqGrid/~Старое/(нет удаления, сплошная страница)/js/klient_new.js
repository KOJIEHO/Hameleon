const form = document.getElementById('form')

function retrieveFormValue(event){
    event.preventDefault();
    
    fIO = document.form.Surname.value + " " + document.form.Name.value + " " + document.form.Middlename.value
    pasport = document.form.seria.value + " " + document.form.nomer.value
    organizacia = document.form.organizacia.value;
    telefon = document.form.telefon.value;

    data = [{
        "$type": "Klient",
        "FIO": fIO,
        "Pasport": pasport,
        "Organizaciya": organizacia,
        "Telefon": telefon,
        }]
    fetch("http://localhost:4388/ham/odata/Klient", {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            "Content-type": "application/json"
        }       
    })
        .then((response) => response.json())
        .then((json) => console.log(json));
}

form.addEventListener('submit', retrieveFormValue)
