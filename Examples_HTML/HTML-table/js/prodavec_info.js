function addDataFromDataBase() {
    fetch('http://localhost:4388/ham/odata/Prodavec?$expand=prodagi')
    .then(response => response.json())
    .then(response => {
        let table = document.getElementById("outputTable");
        let i = 0;
        while (i < response.value.length){
            let newRow = table.insertRow(i + 1);

            if (response.value[i].prodagi != '[]'){
                prodagi = response.value[i].Prodagi.length
            } else{
                prodagi = 'Продаж нет'
            }

            newRow.insertCell(0).innerHTML = response.value[i].$id; 
            newRow.insertCell(1).innerHTML = response.value[i].FIO; 
            newRow.insertCell(2).innerHTML = response.value[i].Telefon; 
            newRow.insertCell(3).innerHTML = response.value[i].Prinyat; 
            newRow.insertCell(4).innerHTML = response.value[i].DataRogdeniya; 
            newRow.insertCell(5).innerHTML = prodagi; 
            newRow.insertCell(6).innerHTML = 
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
    let telefon = document.getElementById("TelefonInput").value; 
    let prinyat = document.getElementById("PrinyatInput").value; 
    let datarogdeniya = document.getElementById("DataRogdeniyaInput").value;  

    data = [{
        "$type": "Prodavec",
        "FIO": fio,
        "Telefon": telefon,
        "Prinyat": prinyat,
        "DataRogdeniya": datarogdeniya,
        }]

    fetch("http://localhost:4388/ham/odata/Prodavec", {
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
        newRow.insertCell(2).innerHTML = telefon; 
        newRow.insertCell(3).innerHTML = prinyat; 
        newRow.insertCell(4).innerHTML = datarogdeniya; 
        newRow.insertCell(5).innerHTML = "0";
        newRow.insertCell(6).innerHTML = 
            '<button onclick="editData(this)">Edit</button>' + 
            '<button onclick="deleteData(this)">Delete</button>';
    })
    clearInputs();
} 


function editData(button) { 
    let row = button.parentNode.parentNode; 

    let id = row.cells[0].innerHTML;
    let fioCell = row.cells[1];
    let telefonCell = row.cells[2]; 
    let prinyatCell = row.cells[3]; 
    let datarogdeniyaCell = row.cells[4];

    let fioInput = prompt("Enter the updated FIO:", fioCell.innerHTML); 
    let telefonInput = prompt("Enter the updated Telefon:", telefonCell.innerHTML); 
    let prinyatInput = prompt("Enter the updated Data Prinyat:", prinyatCell.innerHTML); 
    let datarogdeniyaInput = prompt("Enter the updated DataRogdeniya:", datarogdeniyaCell.innerHTML); 
    
    fioCell.innerHTML = fioInput; 
    telefonCell.innerHTML = telefonInput; 
    prinyatCell.innerHTML = prinyatInput; 
    datarogdeniyaCell.innerHTML = datarogdeniyaInput; 

    data = [{
        "$id": id,
        "$type": "Prodavec",
        "FIO": fioInput,
        "Telefon": telefonInput,
        "Prinyat": prinyatInput,
        "DataRogdeniya": datarogdeniyaInput,
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
        "$type": "Prodavec"
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
    document.getElementById("TelefonInput").value = ""; 
    document.getElementById("PrinyatInput").value = "";
    document.getElementById("DataRogdeniyaInput").value = ""; 
} 
