function saveAs(content, fileName) {
    const a = document.createElement("a");
    const isBlob = content.toString().indexOf("Blob") > -1;
    let url = content;
    if (isBlob) {
      url = window.URL.createObjectURL(content);
    }
    a.href = url;
    a.download = fileName;
    a.click();
    if (isBlob) {
      window.URL.revokeObjectURL(url);
    }
}


function retrieveFormValue(event){
    event.preventDefault();
    
    fetch('http://localhost:4388/ham/odata/Prodavec?$expand=prodagi')
    .then(response => response.json())
    .then(response => 
        $(function () 
        {
            data = [["Номер", "ФИО", "Телефон", "Принят", "Дата рождения", "Продажи"]]
            
            let i = 0;
            while (i < response.value.length){
                if (response.value[i].prodagi != '[]'){
                    prodagi = response.value[i].Prodagi.length
                } else{
                    prodagi = 'Продаж нет'
                }

                data.push([i+1, String(response.value[i].FIO), String(response.value[i].Telefon), String(response.value[i].Prynyat), String(response.value[i].DataRogdeniya), String(prodagi)]);
                i++;
            };
            data = data.map(function(el){ return [el[0], ' ' + el[1] + ', ' + el[2] + ', ' + el[3] + ', ' + el[4] + ', ' + el[5]].join(',') + "\r\n"; });
            saveAs( new Blob( data, {type : 'text/csv;charset=utf-8'}), 'prodavec_info.csv' );
        })
    
    )

}

form.addEventListener('submit', retrieveFormValue)
