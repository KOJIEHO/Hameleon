const form = document.getElementById('form')

function retrieveFormValue(event){
    event.preventDefault();

    fetch('http://localhost:4388/ham/odata/Klient(1001,1002)?$metadata=columns')
        .then(response => response.json())
        .then(
            function(response){ 
                tableData = response.value
                inputCount = Object.keys(tableData[0]).length

                inputInfo = []
                data = {}
                for (let i = 0; i < inputCount; i++) {
                    data[Object.keys(tableData[0])[i]] = document.form[i].value
                } 
                
                fetch("http://localhost:4388/ham/odata/Klient", {
                    method: "POST",
                    body: JSON.stringify([data]),
                    headers: {"Content-type": "application/json"}       
                    })
                    .then((response) => response.json())
                    .then((json) => console.log(json))
            }
        )      
}

form.addEventListener('submit', retrieveFormValue)
