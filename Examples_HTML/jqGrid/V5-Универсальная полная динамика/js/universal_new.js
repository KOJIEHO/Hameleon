const form = document.getElementById('form')
user = document.currentScript.getAttribute('user')


function retrieveFormValue(event){
    event.preventDefault();

    url = `http://localhost:4388/ham/odata/${user}(nil)?$metadata=columns`
    fetch(url)
        .then(response => response.json())
        .then(
            function(response){
                data = response.columns
                for (i = 0; i < data.length; i++){if (data[i].name[0] == "$"){delete data.splice(i, 1);i--}}

                key = []
                for (i = 0; i < data.length; i++){
                    if (data[i].name){key.push(data[i].name)}
                }
                
                POST_info = {}
                for (let i = 0; i < data.length; i++) {
                    POST_info[key[i]] = document.form[i].value
                } 

                fetch(`http://localhost:4388/ham/odata/${user}`, {
                    method: "POST",
                    body: JSON.stringify([POST_info]),
                    headers: {"Content-type": "application/json"}       
                    })
            }
        )      
}

form.addEventListener('submit', retrieveFormValue)
