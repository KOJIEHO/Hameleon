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
            try {textarea.remove()} catch (err) {}
            $('#grid').jqGrid('GridUnload')

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

                colSettings = [] 
                for (i=0; i < tableSettings.length; i++) {
                    if (tableSettings[i].name){colName = tableSettings[i].name}else{colName = ''}
                    if (tableSettings[i].caption){colCaption = tableSettings[i].caption}else{colCaption = ''}
                    if (tableSettings[i].type){colType = tableSettings[i].type}else{colType = ''}
                    if (tableSettings[i].length){colLenght = tableSettings[i].length}else{colLenght = ''}
                    colSettings.push({name: colName, caption: colCaption, type: colType, length: colLenght, align:'center'})
                }
                jQuery('#grid').jqGrid({colModel: colSettings, data: tableData});
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
        }
    )
}