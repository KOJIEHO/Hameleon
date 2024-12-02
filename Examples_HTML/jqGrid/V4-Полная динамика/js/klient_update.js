const form = document.getElementById('form')
id = new URLSearchParams(window.location.search).get('idKlient');

function klient_update(){

    fetch('http://localhost:4388/ham/odata/Klient(1001,1002)?$metadata=columns')
        .then(response => response.json())
        .then(
            function(response){ 
                tableData = response.value
                inputCount = Object.keys(tableData[0]).length

                inputInfo = []
                data = {"$id": id,
                    "$type": "Klient"
                }
                for (let i = 0; i < inputCount; i++) {
                    if (document.form[i].value != ''){
                        data[Object.keys(tableData[0])[i]] = document.form[i].value
                    }
                    
                } 
                console.log([data])

                fetch("http://localhost:4388/ham/odata", {
                    method: "PUT",
                    body: JSON.stringify(data),
                    headers: {
                        "Content-type": "application/json"
                    }       
                })
                    .then((response) => response.json())
                    .then((json) => console.log(json))
                
            }
        ) 
    
    // data = [{
    //     "$id": id,
    //     "$type": "Klient",
    //     "FIO": fIO,
    //     "Pasport": pasport,
    //     "Organizaciya": organizacia,
    //     "Telefon": telefon,
    // }]
    
}


function klient_delete(){
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
