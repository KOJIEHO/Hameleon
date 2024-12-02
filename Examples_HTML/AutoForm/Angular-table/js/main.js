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
            try {body.remove()} catch (err) {}
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

                body = document.createElement("body")
                body.setAttribute("ng-app", "myApp")
                form.appendChild(body);

                div = document.createElement("div")
                div.setAttribute("ng-controller", "AppCtrl")
                body.appendChild(div);
                
                table = document.createElement("table")
                div.appendChild(table);
                tbody = document.createElement("tbody")
                table.appendChild(tbody);

                colNameLength = colName.length
                trHead = document.createElement("tr")
                for (i = 0; i < colNameLength; i++) {
                    th = document.createElement('th')
                    th.textContent = colName[i]
                    trHead.appendChild(th);
                }
                tbody.appendChild(trHead);              

                tr = document.createElement("tr")
                tr.setAttribute("ng-repeat", "item in mytab") 
                for (i = 0; i < colNameLength; i++) {
                    td = document.createElement('td')
                    td.textContent = `{{item.${colName[i]}}}`
                    tr.appendChild(td);
                }
                tbody.appendChild(tr)
        
                var myApp = angular.module('myApp', []);
                console.log("12135213");
                myApp.controller("AppCtrl", function($scope, $http) {
                    console.log("12135213");
                    $scope.mytab = [{"modelj": "Загрузка"}];
                    $http.get(url)
                    .then(function(response) {
                        console.log(response.data.value);
                        $scope.mytab = response.data.value;
                    });
                });	
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