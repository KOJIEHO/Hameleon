function main(){
    const form = document.getElementById('form')
    restValue = document.form[0].value
    url = document.form[1].value
    body = document.form[2].value
    if (restValue == "GET"){get(url)}
    if (restValue == "POST"){post(url, body)}
}


function get(url){
    localhost = "http://localhost:4388"
    metadata = "?$metadata=columns"

    index = url.indexOf(localhost)
    if (index == -1){url = localhost + url}
    index = url.indexOf(metadata)
    if (index == -1){
        index = url.indexOf("?")
        if (index == -1){url = url + metadata} else{url = url + metadata.slice(1)}
    }
    
    fetch(url)
    .then(response => response.json())
    .then(response => 
        $(function (){
            var form = document.getElementById("tableForm")
            form.setAttribute("style", "display:flex;flex-direction:column")
            try {table.remove()} catch (err) {}
            try {textarea.remove()} catch (err) {}

            if (!response.columns){
                if (response.error){
                    textarea = document.createElement("textarea")
                    textarea.setAttribute("class", "w-50")
                    textarea.textContent = `Code: ${response.error.code}\nMessage: ${response.error.message}`
                    form.appendChild(textarea)
                } else {
                    textarea = document.createElement("textarea")
                    textarea.setAttribute("class", "w-50")
                    textarea.textContent = "Message: Bad Request"
                    form.appendChild(textarea)
                }
            } else {
                tableSettings = response.columns 
                tableData = response.value

                colName = [] 
                for (i = 0; i < tableSettings.length; i++) {if (tableSettings[i].name){colName.push(tableSettings[i].name)}else{colName.push('')}}

                table = document.createElement("table")
                table.setAttribute("id", "outputTable")
                tr = document.createElement("tr")
                
                for (i = 0; i < colName.length; i++) {
                    th = document.createElement('th')
                    th.textContent = colName[i]
                    tr.appendChild(th);
                }
                table.appendChild(tr);
                form.appendChild(table);

                rowCount = tableData.length
                key_tableData = Object.keys(tableData[0])
                columnCount = key_tableData.length                
                for (i = 0; i < rowCount; i++) {
                    newRow = table.insertRow(i + 1);
                    for (k = 0; k < columnCount; k++) {newRow.insertCell(k).innerHTML = tableData[i][key_tableData[k]]}
                }
            }       
        })   
    )
      
}


function post(url, data){
    localhost = "http://localhost:4388"

    index = url.indexOf(localhost)
    if (index == -1){url = localhost + url}  

    fetch(url, {
        method: "POST",
        body: JSON.stringify(data),
        headers: {"Content-type": "application/json"}       
    })
    .then(response => response.json())
    .then(json => console.log(json))
}