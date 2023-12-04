const form = document.getElementById('form')


function retrieveFormValue(event){
    event.preventDefault();

    const Surname = document.form.Surname.value;
    const Name = document.form.Name.value;
    const Middlename = document.form.Middlename.value;
    const seria = document.form.seria.value;
    const nomer = document.form.nomer.value;
    const organizacia = document.form.organizacia.value;
    const telefon = document.form.telefon.value;

    fetch("http://localhost:4388/ham/sql/SetNextHamId?id=1401", {
        method: "POST",
        body: [{
        "$type": "Klient",
        "fIO": Surname + " " + Name + " " + Middlename,
        "pasport": seria + nomer,
        "organizaciya": organizacia,
        "telefon": telefon,
        "status": 0
        }],
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    })
        .then((response) => response.json())
        .then((json) => console.log(json));

    qwer = [{
        "$type": "Klient",
        "fIO": Surname + " " + Name + " " + Middlename,
        "pasport": seria + " " + nomer,
        "organizaciya": organizacia,
        "telefon": telefon,
        "status": 0
        }]

    console.log(qwer)
}

form.addEventListener('submit', retrieveFormValue)
