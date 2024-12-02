fetch('http://localhost:4388/ham/odata/Klient?$expand=pokupki/mashiny,pokupki/prodavec')
    .then(response => response.json())
    .then(response => 
        $(function () 
        {            
            const data = [];
            const colName = [
                { name: "ID" },
                { name: "FIO"},
                { name: "Pasport"},
                { name: "Orga"},
                { name: "Telefon"}
            ];

            let i = 0;
            while (i < response.value.length){
                data.push({id: i+1, ID: response.value[i].$id, FIO: response.value[i].FIO, Pasport: response.value[i].Pasport, Orga: response.value[i].Organizaciya, Telefon: response.value[i].Telefon });
                i++;
            };

            "use strict";
                $("#grid").jqGrid({
                    colModel: colName, 
                    data: data,
                });
        })
    
    )