function addDataFromDataBase() {
    fetch('http://localhost:4388/ham/odata/Klient?$expand=pokupki/mashiny,pokupki/prodavec')
    .then(response => response.json())
    .then(response => {
        let table = document.getElementById("outputTable");
        let i = 0;
        while (i < response.value.length){
            let newRow = table.insertRow(i + 1);

            newRow.insertCell(0).innerHTML = response.value[i].$id; 
            newRow.insertCell(1).innerHTML = response.value[i].FIO; 
            newRow.insertCell(2).innerHTML = response.value[i].Pasport; 
            newRow.insertCell(3).innerHTML = response.value[i].Organizaciya; 
            newRow.insertCell(4).innerHTML = response.value[i].Telefon; 
            newRow.insertCell(5).innerHTML = 
                '<button onclick="editData(this)">Edit</button>'+ 
                '<button onclick="deleteData(this)">Delete</button>'; 
            i++;     
        }; 
    }) 
}
addDataFromDataBase();


function addData() { 
    let table = document.getElementById("outputTable"); 
    let newRow = table.insertRow(table.rows.length);

    let fio = document.getElementById("FioInput").value; 
    let pasport = document.getElementById("PasportInput").value; 
    let organizacia = document.getElementById("OrgaInput").value; 
    let telefon = document.getElementById("TelefonInput").value; 
    
    data = [{
        "$type": "Klient",
        "FIO": fio,
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
    .then((response) => {
        newRow.insertCell(0).innerHTML = response.NewIDs[0];
        newRow.insertCell(1).innerHTML = fio; 
        newRow.insertCell(2).innerHTML = pasport; 
        newRow.insertCell(3).innerHTML = organizacia; 
        newRow.insertCell(4).innerHTML = telefon; 
        newRow.insertCell(5).innerHTML = 
            '<button onclick="editData(this)">Edit</button>' + 
            '<button onclick="deleteData(this)">Delete</button>'; 
    })
    clearInputs();
} 


function editData(button) { 
    let row = button.parentNode.parentNode; 

    let id = row.cells[0].innerHTML;
    let fioCell = row.cells[1];
    let pasportCell = row.cells[2]; 
    let orgaCell = row.cells[3]; 
    let telefonCell = row.cells[4];

    let fioInput = prompt("Enter the updated FIO:", fioCell.innerHTML); 
    let pasportInput = prompt("Enter the updated Pasport:", pasportCell.innerHTML); 
    let orgaInput = prompt("Enter the updated Orga:", orgaCell.innerHTML); 
    let telefonInput = prompt("Enter the updated Telefon:", telefonCell.innerHTML); 
    
    fioCell.innerHTML = fioInput; 
    pasportCell.innerHTML = pasportInput; 
    orgaCell.innerHTML = orgaInput; 
    telefonCell.innerHTML = telefonInput; 

    data = [{
        "$id": id,
        "$type": "Klient",
        "FIO": fioInput,
        "Pasport": pasportInput,
        "Organizaciya": orgaInput,
        "Telefon": telefonInput,
    }]
    fetch("http://localhost:4388/ham/odata", {
        method: "PUT",
        body: JSON.stringify(data),
        headers: {
            "Content-type": "application/json"
        }       
    })
    // .then((response) => response.json())
    // .then((json) => console.log(json));
} 


function deleteData(button) {  
    let row = button.parentNode.parentNode; 

    let id = row.cells[0].innerHTML;
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
    // .then((response) => response.json())
    // .then((json) => console.log(json)); 

    row.parentNode.removeChild(row); 
} 


function clearInputs() { 
    document.getElementById("FioInput").value = ""; 
    document.getElementById("PasportInput").value = ""; 
    document.getElementById("OrgaInput").value = "";
    document.getElementById("TelefonInput").value = ""; 
} 