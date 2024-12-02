const form = document.getElementById('form')
id = new URLSearchParams(window.location.search).get('idUser');

user = document.currentScript.getAttribute('user')
num = document.currentScript.getAttribute('num')

url = `http://localhost:4388/ham/odata/${user}${num}?$metadata=columns`


function update(){
    fetch(url)
        .then(response => response.json())
        .then((function (response){ 
                inputCount = response.columns
                for (i = 0; i < inputCount.length; i++){if (inputCount[i].name[0] == "$"){delete inputCount.splice(i, 1);i--}}

                data = {"$id": id, "$type": "Klient"}
                for (let i = 0; i < inputCount.length; i++){if (document.form[i].value != ''){data[inputCount[i].name] = document.form[i].value}} 

                console.log(data);
                fetch("http://localhost:4388/ham/odata", {
                    method: "PUT",
                    body: JSON.stringify([data]),
                    headers: {"Content-type": "application/json"}       
                })
            }
        ))         
}


function deletion(){
    data = [{"$id": id, "$type": user}]
    fetch("http://localhost:4388/ham/odata/", { 
        method: "DELETE",
        body: JSON.stringify(data),
        headers: {"Content-type": "application/json"}
    })
}
