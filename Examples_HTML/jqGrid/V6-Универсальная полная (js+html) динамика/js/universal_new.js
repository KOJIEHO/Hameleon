class_name = new URLSearchParams(window.location.search).get('Class_name')

function new_user(){
    fetch(`http://localhost:4388/ham/odata/${class_name}(nil)?$metadata=columns`)
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

                fetch(`http://localhost:4388/ham/odata/${class_name}`, {
                    method: "POST",
                    body: JSON.stringify([POST_info]),
                    headers: {"Content-type": "application/json"}       
                    })
                window.location.href = `list_objects.html?Class_name=${class_name}`
            }
        )      
}
