class_name = new URLSearchParams(window.location.search).get('Class_name')
id = new URLSearchParams(window.location.search).get('id');

function update(){
    fetch(`http://localhost:4388/ham/odata/${class_name}(nil)?$metadata=columns`)
        .then(response => response.json())
        .then((function (response){             
                inputCount = response.columns
                for (i = 0; i < inputCount.length; i++){if (inputCount[i].name[0] == "$"){delete inputCount.splice(i, 1);i--}}

                data = {"$id": id, "$type": class_name}
                for (let i = 0; i < inputCount.length; i++){if (document.form[i].value != ''){data[inputCount[i].name] = document.form[i].value}} 

                fetch("http://localhost:4388/ham/odata", {
                    method: "PUT",
                    body: JSON.stringify([data]),
                    headers: {"Content-type": "application/json"}       
                })
            }
        )) 
    setTimeout(function () {window.location.href = `list_objects.html?Class_name=${class_name}`}, 500);        
}


function deletion(){
    data = [{"$id": id, "$type": class_name}]
    fetch("http://localhost:4388/ham/odata/", { 
        method: "DELETE",
        body: JSON.stringify(data),
        headers: {"Content-type": "application/json"}
    })
    window.location.href = `list_objects.html?Class_name=${class_name}`
}
